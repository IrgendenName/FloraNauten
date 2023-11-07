<script>
    import { onMount } from "svelte";
    import axios from "axios";

    let base_url = "http://127.0.0.1:5000";
    let canvas;
    let context;

    // When true, moving the mouse draws on the canvas
    let isDrawing = false;
    let x = 0;
    let y = 0;

    let prediction;

    onMount(() => {
        context = canvas.getContext("2d");
        context.lineWidth = 50;
        context.fillStyle = "#ffffff";
        context.fillRect(0, 0, canvas.width, canvas.height);
        context.globalCompositeOperation = "source-over";
        // event.offsetX, event.offsetY gives the (x,y) offset from the edge of the canvas.

        // Add the event listeners for mousedown, mousemove, and mouseup
        canvas.addEventListener("mousedown", (e) => {
            x = e.offsetX;
            y = e.offsetY;
            isDrawing = true;
        });

        canvas.addEventListener("mousemove", (e) => {
            if (isDrawing) {
                drawLine(context, x, y, e.offsetX, e.offsetY, e);
                x = e.offsetX;
                y = e.offsetY;
            }
        });

        window.addEventListener("mouseup", (e) => {
            if (isDrawing) {
                drawLine(context, x, y, e.offsetX, e.offsetY, e);
                x = 0;
                y = 0;
                isDrawing = false;
            }
        });
    });

    function drawLine(context, x1, y1, x2, y2, e) {
        context.beginPath();
        context.strokeStyle = "black";
        context.lineWidth = 25;
        context.moveTo(x1, y1);
        context.lineJoin = context.lineCap = "round";
        context.lineTo(x2, y2);
        context.stroke();
        context.closePath();
    }

    function resetCanvas() {
        context.clearRect(0, 0, canvas.width, canvas.height);
        context.fillStyle = "#ffffff";
        context.fillRect(0, 0, canvas.width, canvas.height);

        document.getElementById("middle_text").style.display = "none";
        document.getElementById("img").style.display = "none";
    }

    function predict() {        
        //console.log(canvas.toDataURL());
        let url = base_url + "/hook";
        console.log(url);
        axios
            .post(
                url,
                {
                    image: canvas.toDataURL(), // remove alpha channel
                },
                {
                    headers: {
                        "Content-Type": "application/json",
                    },
                }
            )
            .then((response) => {
                console.log(String(response.data.image));
                console.log(String(response.data.prediction));
                console.log(String(response.data.image));
                let img = document.getElementById("img");
                img.src = response.data.image;
                img.height = 300;
                img.width = 300;
                document.getElementById("middle_text").style.display = "block";
                document.getElementById("img").style.display = "block";

                prediction = response.data.prediction;
            })
            .catch(function (error) {
                if (error.response) {
                    // The request was made and the server responded with a status code
                    // that falls out of the range of 2xx
                    console.log(error.response.data);
                    console.log(error.response.status);
                    console.log(error.response.headers);
                } else if (error.request) {
                    // The request was made but no response was received
                    // `error.request` is an instance of XMLHttpRequest in the browser and an instance of
                    // http.ClientRequest in node.js
                    console.log(error.request);
                } else {
                    // Something happened in setting up the request that triggered an Error
                    console.log("Error", error.message);
                }
                console.log(error.config);
            });
    }
</script>

<h3>Draw a number between 0-9</h3>
<div class="container">
    <div class="row">
        <div class="col col-lg-4">
            <canvas bind:this={canvas} width="300" height="300" />
            <br />
            <button
                type="button"
                class="btn btn-secondary"
                on:click={resetCanvas}>reset</button
            >
            <button type="button" class="btn btn-secondary" on:click={predict}
                >predict</button
            >
        </div>
        <div class="col-md-auto">
            <div id="middle_text" style="display:none;">
                <h3>Model predicted: {prediction}</h3>
                <p>image was rescaled to the following image</p>
            </div>
        </div>
        <div class="col col-lg-4">
            <img
                style="outline: black 3px solid;display:none;"
                id="img"
                alt=""
            />
        </div>
    </div>
</div>

<style>
    canvas {
        outline: black 3px solid;
    }

    img {
        image-rendering: pixelated;
    }
</style>
