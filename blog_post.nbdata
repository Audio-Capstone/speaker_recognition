{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "7a569de7-f323-4f80-9494-e03480ad659b",
   "metadata": {},
   "source": [
    "# Exploring the world of Audio Data"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "9b762844-e946-4ec7-8d2c-df8fc00b0196",
   "metadata": {},
   "source": [
    "## By: Scott Petersen and Daniel Babcock"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "09f687bd-e780-4425-8b69-ffcd70905d87",
   "metadata": {},
   "source": [
    "## Introduction"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "ec8340cd-c58a-4c6a-9dca-dc56ef4a1a44",
   "metadata": {},
   "source": [
    "        Scott and I had never worked with audio data before and had certainly not used it in a machine learning projects in the past. This was what initially drew our interest in this project. That and the fact that audio information is a growing field of application for machine learning. Whether its generating text from speech or interacting with a customer service chatbot over the phone, there are countless ways to use audio data to make our lives easier (maybe not the customer service chatbots though, those are awful). One of the most interesting ways to use audio data is recognizing the unique features of a particular person’s voice. We take the ability to recognize voices for granted, and it’s amazing the progress that have been made with allowing computers to do the same. Scott and I both wanted to better understand what was going on in those kinds of systems, so we decided to tackle Speaker Identification for our capstone project."
   ]
  },
  {
   "cell_type": "markdown",
   "id": "3fe7ff8f-496d-4761-8ea0-13793fc78b2d",
   "metadata": {},
   "source": [
    "## Initial Research and Picking a Dataset"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "2ff66956-1ce4-4ed8-acba-54b4744e548f",
   "metadata": {},
   "source": [
    "        We began our journey with a lot of reading and watching helpful videos on the subject. The Sound of AI channel on YouTube was a particularly awesome resource with a very detailed series of videos on using Audio Data for Machine Learning. Once we had a basic grasp of what needed to be done, we decided on a publicly-available dataset comprised of 31 phone calls available here: Index of /ca/CallFriend/eng-n/0wav (talkbank.org). These 31 phone calls would presumably represent at least 62 speakers (one for each side of the conversation). We believed this data would present some interesting real-world challenges since phone calls can pick up environmental noise and vary in quality based on the equipment being used."
   ]
  },
  {
   "cell_type": "markdown",
   "id": "76aaf8e5-bcb1-4d70-be1c-70eff515fd38",
   "metadata": {},
   "source": [
    "## Exploratory Data Analysis and Potential Issues"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "52bc3184-fe7c-4b91-99c4-b49d5106dd3a",
   "metadata": {},
   "source": [
    "        With our dataset decided on, we began exploring it to get an idea of what kind of cleaning would be necessary. We realized that our data would need a lot of cleaning before we could extract any useful features from it. Primarily splitting the stereo data into individual channels, reducing noise, and removing periods of silence. We also identified a couple major issues that would not be easy to automatically fix such as multiple people talking on one side of the conversation for extended periods of time and some calls that were much shorter than others. We also wanted to create a test dataset that we would not touch until our final model was chosen. This represented 15% of our data for each speaker."
   ]
  },
  {
   "cell_type": "markdown",
   "id": "1c06d188-dcea-478d-b717-876ce7394807",
   "metadata": {},
   "source": [
    "## Early Feature Extraction and a Doomed Attempt at Deep Learning"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "712ae7ed-7692-439e-87c0-a8bd2f70aad0",
   "metadata": {},
   "source": [
    "        Once we had basic preprocessing completed (splitting stereo channels, reducing noise, removing periods of silence, and creating a holdout test dataset) we began to extract some features such as Mel-frequency cepstrum coefficients (MFCCs) with the goal of applying them to some early deep learning methods. While we had read that GMMs were considered the best way to identify speakers for some time (Reynolds, 2000), we thought a deep learning approach would be interesting and a good learning opportunity. Unfortunately, the initial results were abysmal, and we were not able to achieve any decent scores on the validation test sets."
   ]
  },
  {
   "cell_type": "markdown",
   "id": "312a833a-5d05-4829-abcf-246c74ec3b1f",
   "metadata": {},
   "source": [
    "## Focusing on a GMM Solution"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "1944e88a-2be4-496a-ab9d-7f952d64071b",
   "metadata": {},
   "source": [
    "        Given the deep learning setback, we decided to focus on using the GMM solution we had initially researched. This involved training a separate GMM for each of our 62 speakers and then testing audio samples against each of the models. We used several features to train the GMMs, including:\n",
    "\n",
    "    •\tMel-frequency cepstrum coefficients (MFCCs)\n",
    "    •\t1st and 2nd order Delta MFCCs (26, 13x2)\n",
    "    •\tFrame Root Mean Square\n",
    "    •\tSpectral Centroid\n",
    "    •\tZero Crossing Rate\n",
    "\n",
    "    We also needed to optimize our GMM models, so we used the average BIC and AIC scores of the 62 models to determine which value to use for the n_component parameter. We decided 3 would be the best choice based on the results.\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "b6ec5135-f4eb-4820-9566-817ed4f8af9f",
   "metadata": {},
   "source": [
    "## GMM Solution Evaluation"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "f2bf93bf-fb7f-4d7b-804c-8256234d1f90",
   "metadata": {},
   "source": [
    "        With our model trained and tested, we did a final evaluation of the results on our 15% hold out test dataset. The results were pleasantly surprising, and after removing the results for one speaker for whom we didn’t have enough data, we were able to accurately identify 40 out of 61 of our speakers achieving an accuracy of 65.8%. Considering the challenges present in our dataset and our nascent understanding of audio data, we were encouraged by the fact that our models was able to perform as well as it did."
   ]
  },
  {
   "cell_type": "markdown",
   "id": "aeddf3d2-0a33-4310-8bf0-fb81c60e455e",
   "metadata": {},
   "source": [
    "## Next Steps"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "d8f2b679-a8f2-4e84-ad07-2ac658d1cc40",
   "metadata": {},
   "source": [
    "        While we have only really begun to scratch the surface of all there is to know about this field, we learned a lot while we worked on this project and are eager to continue exploring the world of audio data.  Some of the things we would like to focus on next for this project include:\n",
    "        \n",
    "    •\tPerform speaker diarization to separate out individual speakers in the same audio sample\n",
    "    •\tExploring new pre-processing techniques to better deal with periods of silence and noise\n",
    "    •\tTraining a speaker-independent Universal Background Model (UBM) to be our “unknown speaker” model (if you don’t match any of the knowns, you should match this one)\n",
    "    •\tTurn the preprocessing and modeling into a pipeline that can be made into an API\n",
    "    \n",
    "    Overall, this was an enjoyable foray into a field that neither of us had any experience in. While we ran into a lot of problems and experienced several setbacks, we came away with an appreciation for audio data and a better understanding of the data science process.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "990af6e9-8ed0-4687-9aba-8a6743d0f5e6",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
