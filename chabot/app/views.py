
import pprint
from django.shortcuts import render
import google.generativeai as palm
from app.forms import GenerateTextForm

# Create your views here.
# AIzaSyCZROfI20BJBb-nk5-b39NEJJ1KYgVh2Eo


def generate_text(request):
    # Ensure the request has the 'prompt' parameter
    if request.method == 'POST':
        form = GenerateTextForm(request.POST)
        if form.is_valid():
            prompt = form.cleaned_data['prompt']

            palm.configure(api_key='AIzaSyCZROfI20BJBb-nk5-b39NEJJ1KYgVh2Eo')

            # List available models
            models = [m for m in palm.list_models() if 'generateText' in m.supported_generation_methods]

            if not models:
                return render(request, 'generate_text.html', {'error': 'No models available for text generation'})

            # Select the first available model
            model = models[0].name

            # Generate text
            completion = palm.generate_text(
                model=model,
                prompt=prompt,
                temperature=0,
                max_output_tokens=800
            )

            generated_text = completion.result

            # Render the HTML template with the generated text
            return render(request, 'generate_text.html', {'form': form, 'generated_text': generated_text})

    else:
        form = GenerateTextForm()

    return render(request, 'generate_text.html', {'form': form})

# def generate_prompt():
#     palm.configure(api_key='AIzaSyCZROfI20BJBb-nk5-b39NEJJ1KYgVh2Eo')
#     models = [m for m in palm.list_models() if 'generateText' in m.supported_generation_methods]
#     model = models[0].name
#     completion = palm.generate_text(
#     model=model,
#     prompt="prompt",
#     temperature=0,
#     max_output_tokens=800)

#     print(completion.result)

