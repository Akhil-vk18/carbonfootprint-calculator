def generate_co2_animation():
    return """
    <style>
    @keyframes co2rise {
        0% { transform: translateY(0); }
        100% { transform: translateY(-100%); }
    }
    .co2-container {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        overflow: hidden;
        z-index: -1;
    }
    .co2-animation {
        position: absolute;
        top: 100%;
        left: 0;
        width: 100%;
        height: 200%;
        background-image: url('https://giphy.com/gifs/weather-climate-co2-d2YW4ockfm62BCpy');
        animation: co2rise 20s linear infinite;
    }
    </style>
    <div class="co2-container"><div class="co2-animation"></div></div>
    """

