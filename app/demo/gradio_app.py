import gradio as gr

from core.settings import custom_logger, get_config
from core.modules.model import SentimentClassificationModel


logger = custom_logger("Gradio Demo")


model = SentimentClassificationModel(**get_config("ModelConfig"))


def gradio_predict(text: str):
    """Function for predicting the sentiment given a text"""

    # Model inference
    outputs = model.predict([text])[0]
    return {
        "positive": outputs.positive_score,
        "neutral": outputs.neutral_score,
        "negative": outputs.negative_score,
    }


def create_gradio_demo() -> gr.Interface:
    """Function for creating the Gradio demo interface"""

    theme = gr.themes.Monochrome()
    demo = gr.Blocks(theme=theme)
    with demo:
        with gr.Row():
            gr.Markdown(
                """
                # <center> Multilingual Sentiment Classification App </center>
                ### <center> Application for predicting the sentiment within a text</center>
                """
            )
        with gr.Row():
            with gr.Column():
                input_text = gr.components.Textbox(
                    placeholder="Write your sentence here"
                )
                predict_btn = gr.Button(value="Predict")
                examples = gr.Examples(
                    examples=[
                        "It wasn't that bad, it was ok",
                        "Me gustaron mucho los personajes secundarios!",
                        "Eu não gostei nada disso, eu ficava entediado o tempo todo",
                    ],
                    inputs=input_text,
                )
            with gr.Column():
                classification_labels = gr.components.Label(
                    num_top_classes=3, label="Classification results"
                )

        predict_btn.click(
            gradio_predict,
            inputs=[input_text],
            outputs=[classification_labels],
        )

    demo.queue(concurrency_count=1)
    return demo
