# PaddyLab

Deep learning tool for Paddy disease identification & classification. 

Its an end to end project starting from training a Deep learning model on [Kaggle Paddy Doctor dataset](https://www.kaggle.com/competitions/paddy-disease-classification/data) and then using our trained model to create an API with [Gradio](https://www.gradio.app/) and then integrating this API with Desktop application to run inference on local machine. 

For an obvious reason, this project is very personal to me because my father has been a Paddy farmer and I have grown up seeing Paddy fields better part of my childhood and even today if go home I’m surrounded by lush Green Paddy fields in our village. So, I have a deep personal connection to what I'm doing with this project.

## How to use:

**Step 0:** Take a closeup photo of a Paddy plant and make sure to capture impacted parts of the leafs properly

**Setp 1:** Then click on `Browse` button and upload your photo

**Step 2:** Click on `Predict` button and wait for few seconds

`Note: Make sure you have a working internet connection`

**Step 3:** In few seconds you will have predictions and the prediction confidence level shown in the message box


## Limitations

- Since the Paddy plant is part of `Grass Family` you can easily fool this deep learning model by uploading a photo of a Grass and you will get some kind of predictions
- Nothing is 100% perfect, so there is always a room for improvement and no exception for this model as well


## What next

- Converting the first limitation to an opportunity by training another deep learning model to first recognize whether an image is Paddy plant or not and that will act as a gate before the actual prediction


## UI Screenshots

Default User interface when its fully loaded

!['Default UI'](/img/Default_UI.png)

User interface during inference stage

![](/img/Inference_UI.png)


## Credits

- [Kaggle Paddy Doctor dataset](https://www.kaggle.com/competitions/paddy-disease-classification/data)
- [FastAI](https://www.fast.ai/)
- [Gradio](https://www.gradio.app/)
- [Gradio Client](https://github.com/gradio-app/gradio/blob/main/client/python/README.md)
- [Huggingface Spaces](https://huggingface.co/spaces)
- [svgrepo ](https://www.svgrepo.com/)
