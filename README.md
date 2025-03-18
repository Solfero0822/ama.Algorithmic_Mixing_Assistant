# Alogithmic Mixing Assistant (ama) using PyTorch

- Building a software to assist with the process of Music Mixing

## Description 📝

    This project aims to develop an algorithmic music mixing assistant designed to support sound engineers in achieving a mix.

    The assistant will analyze user-provided reference tracks (2-3) and the current mix, offering suggestions on EQ curves, panning, compression, tonal quality and peak RMS/LUFS measurements.

    This assistant will function solely as a suggester, allowing users
    to make independent decisions and explore creative solutions.
    While beginners will use the tool to achieve technical standards more efficiently, professional engineers may find it valuable as it may provide possible solutions to a problem.

    Success will be measured by the assistant's ability to offer suggestions that positively influence the mix, bringing it closer to the reference tracks and empowering users to preserve the
    individuality and creative process in their mixes.

## Goals 🧑🏽‍💻

    To research and understand the process of building audio software tools, while learning the application of neural network and deep learning.

    This will support my pursuit to understand the workings behind an audio plug-in while equipping me with the skills require for it.

## How it works

    Taking user-provided reference tracks and

## File Locations

    File Location can be set by the user through ama_ui.py

## Packages

    The packages are required to run the program and must be installed in order to run the code

    Make sure they are installed into ama_env/lib/python3.10/site-packages

    For Core Code

        run
            pip install torch torchaudio certifi openunmix

    - torch is PyTorch (for neural network)
    - torchaudio is Torchaudio (for audio processing)
    - certifi is Certifi (to verify SSL/TLS certificates)
    - openunmix is Open-Unmix (for audio separation)

    For Visualization

        run
            pip install librosa matplotlib

    - librosa is librosa (for audio analysis)
    - matplotlib is matplotlib (for creating static, animated, and interactive visualizations)

    For Prototyping

        run
            pip install ipykernel (dependency for Jupiter notebook)
