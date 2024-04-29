from flask import Flask, render_template, request, jsonify
from transformers import GPT2LMHeadModel, GPT2Tokenizer
import torch

app = Flask(__name__)
tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
model = GPT2LMHeadModel.from_pretrained("gpt2")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/generate-story", methods=["POST"])
def generate_story():
    try:
        prompt = request.form.get("prompt", "")
        input_ids = tokenizer.encode(prompt, return_tensors="pt")
        attention_mask = torch.ones_like(input_ids)  # Create attention mask
        output = model.generate(input_ids, attention_mask=attention_mask, max_length=200, num_return_sequences=1)
        generated_story = tokenizer.decode(output[0], skip_special_tokens=True)
        return jsonify({"story": generated_story})
    except Exception as e:
        return jsonify({"error": str(e)})


if __name__ == "__main__":
    app.run(debug=True)
