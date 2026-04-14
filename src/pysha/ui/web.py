"""FastAPI web interface — REST + WebSocket chat.

Install with: ``pip install 'pysha[web]'``
Run via: ``pysha web``
"""

from __future__ import annotations

from typing import Any

from pysha.app import Assistant


def build_app(assistant: Assistant) -> Any:
    """Construct a FastAPI application bound to *assistant*."""
    try:
        from fastapi import FastAPI, WebSocket, WebSocketDisconnect
        from fastapi.responses import HTMLResponse
        from pydantic import BaseModel
    except ImportError as exc:  # pragma: no cover
        raise RuntimeError("Install the web extra: pip install 'pysha[web]'") from exc

    app = FastAPI(title=f"{assistant.settings.assistant_name} API", version="2.0.0")

    class ChatRequest(BaseModel):
        message: str

    class ChatResponse(BaseModel):
        reply: str

    @app.on_event("startup")
    async def _startup() -> None:
        await assistant.start()

    @app.on_event("shutdown")
    async def _shutdown() -> None:
        await assistant.stop()

    @app.get("/", response_class=HTMLResponse)
    async def index() -> str:
        return _INDEX_HTML.replace("__NAME__", assistant.settings.assistant_name)

    @app.get("/healthz")
    async def health() -> dict[str, Any]:
        return {
            "status": "ok",
            "session": assistant.session_id,
            "engines": {
                "stt": assistant.stt.name if assistant.stt else None,
                "tts": assistant.tts.name if assistant.tts else None,
                "llm": assistant.llm.name if assistant.llm else None,
            },
            "skills": sorted(assistant.skills),
        }

    @app.post("/chat", response_model=ChatResponse)
    async def chat(req: ChatRequest) -> ChatResponse:
        return ChatResponse(reply=await assistant.handle_text(req.message))

    @app.websocket("/ws")
    async def ws(socket: WebSocket) -> None:
        await socket.accept()
        try:
            while True:
                text = await socket.receive_text()
                reply = await assistant.handle_text(text)
                await socket.send_json({"role": "assistant", "content": reply})
        except WebSocketDisconnect:
            return

    return app


_INDEX_HTML = """<!doctype html>
<html>
<head>
  <meta charset="utf-8" />
  <title>__NAME__</title>
  <style>
    body { font: 16px system-ui, sans-serif; max-width: 720px; margin: 2rem auto; padding: 0 1rem; background:#0f172a; color:#e2e8f0; }
    h1 { color:#38bdf8; }
    #log { border:1px solid #334155; border-radius:8px; padding:1rem; height:60vh; overflow:auto; background:#1e293b; }
    .msg { margin: .5rem 0; }
    .user { color:#fde68a; }
    .assistant { color:#a7f3d0; white-space: pre-wrap; }
    form { display:flex; gap:.5rem; margin-top:1rem; }
    input { flex:1; padding:.5rem; border-radius:6px; border:1px solid #334155; background:#0f172a; color:#e2e8f0; }
    button { padding:.5rem 1rem; border-radius:6px; border:none; background:#38bdf8; color:#0f172a; font-weight:600; }
  </style>
</head>
<body>
  <h1>__NAME__</h1>
  <div id="log"></div>
  <form id="f"><input id="i" autocomplete="off" placeholder="Ask me anything..." /><button>Send</button></form>
  <script>
    const log = document.getElementById('log');
    const ws = new WebSocket((location.protocol === 'https:' ? 'wss://' : 'ws://') + location.host + '/ws');
    function add(role, text){ const d=document.createElement('div'); d.className='msg '+role; d.textContent=(role==='user'?'you: ':'assistant: ')+text; log.appendChild(d); log.scrollTop=log.scrollHeight; }
    ws.onmessage = e => { const m = JSON.parse(e.data); add(m.role, m.content); };
    document.getElementById('f').addEventListener('submit', e => {
      e.preventDefault();
      const v = document.getElementById('i').value.trim();
      if(!v) return; add('user', v); ws.send(v); document.getElementById('i').value='';
    });
  </script>
</body>
</html>
"""
