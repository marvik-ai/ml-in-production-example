import gradio as gr
import uvicorn

from app import create_app
from app.demo.gradio_app import create_gradio_demo
from core.settings import custom_logger


logger = custom_logger("Main API")


app = create_app()
gradio_demo = create_gradio_demo()
app = gr.mount_gradio_app(app, gradio_demo, path="/demo")


# Run API
if __name__ == "__main__":
    logger.info("Running FastAPI with uvicorn")
    uvicorn.run(app, host="0.0.0.0", port=80)
