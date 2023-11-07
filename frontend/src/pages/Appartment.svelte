<script>
 	import axios from "axios";

	let base_url = 'http://127.0.0.1:5000'
	//let base_url = "https://wanlau01.pythonanywhere.com";
	let bfs_number_names = [
		{id: 261, name: `Zürich` },
		{id: 62, name: `Kloten` },
		{id: 198, name: `Uster` },
		{id: 296, name: `Illnau-Effretikon` },
		{id: 27, name: `Feuerthalen` },
		{id: 177, name: `Pfäffikon` },
		{id: 11, name: `Ottenbach` },
		{id: 191, name: `Dübendorf` },
		{id: 138, name: `Richterswil` },
		{id: 195, name: `Maur` },
		{id: 56, name: `Embrach` },
		{id: 53, name: `Bülach` },
		{id: 230, name: `Winterthur` },
		{id: 157, name: `Oetwil am See` },
		{id: 178, name: `Russikon` },
		{id: 10, name: `Obfelden` },
		{id: 120, name: `Wald (ZH)` },
		{id: 91, name: `Niederweningen` },
		{id: 84, name: `Dällikon` },
		{id: 83, name: `Buchs (ZH)` },
		{id: 118, name: `Rüti (ZH)` },
		{id: 173, name: `Hittnau` },
		{id: 52, name: `Bassersdorf` },
		{id: 58, name: `Glattfelden` },
		{id: 66, name: `Opfikon` },
		{id: 117, name: `Hinwil` },
		{id: 95, name: `Regensberg` },
		{id: 136, name: `Langnau am Albis` },
		{id: 243, name: `Dietikon` },
		{id: 151, name: `Erlenbach (ZH)` },
		{id: 6, name: `Kappel am Albis` },
		{id: 158, name: `Stäfa` },
		{id: 231, name: `Zell (ZH)` },
		{id: 228, name: `Turbenthal` },
		{id: 92, name: `Oberglatt` },
		{id: 72, name: `Winkel` },
		{id: 199, name: `Volketswil` },
		{id: 135, name: `Kilchberg (ZH)` },
		{id: 121, name: `Wetzikon (ZH)` },
		{id: 160, name: `Zumikon` },
		{id: 180, name: `Weisslingen` },
		{id: 219, name: `Elsau` },
		{id: 221, name: `Hettlingen` },
		{id: 139, name: `Rüschlikon` },
		{id: 13, name: `Stallikon` },
		{id: 86, name: `Dielsdorf` },
		{id: 69, name: `Wallisellen` },
		{id: 54, name: `Dietlikon` },
		{id: 156, name: `Meilen` },
		{id: 200, name: `Wangen-Brüttisellen` },
		{id: 28, name: `Flaach` },
		{id: 96, name: `Regensdorf` },
		{id: 90, name: `Niederhasli` },
		{id: 297, name: `Bauma` },
		{id: 241, name: `Aesch (ZH)` },
		{id: 247, name: `Schlieren` },
		{id: 113, name: `Dürnten` },
		{id: 249, name: `Unterengstringen` },
		{id: 115, name: `Gossau (ZH)` },
		{id: 245, name: `Oberengstringen` },
		{id: 98, name: `Schleinikon` },
		{id: 1, name: `Aeugst am Albis` },
		{id: 38, name: `Rheinau` },
		{id: 60, name: `Höri` },
		{id: 225, name: `Rickenbach (ZH)` },
		{id: 67, name: `Rafz` },
		{id: 131, name: `Adliswil` },
		{id: 161, name: `Zollikon` },
		{id: 250, name: `Urdorf` },
		{id: 153, name: `Hombrechtikon` },
		{id: 242, name: `Birmensdorf (ZH)` },
		{id: 172, name: `Fehraltorf` },
		{id: 102, name: `Weiach` },
		{id: 155, name: `Männedorf` },
		{id: 154, name: `Küsnacht (ZH)` },
		{id: 4, name: `Hausen am Albis` },
		{id: 59, name: `Hochfelden` },
		{id: 193, name: `Fällanden` },
		{id: 194, name: `Greifensee` },
		{id: 196, name: `Mönchaltorf` },
		{id: 214, name: `Dägerlen` },
		{id: 39, name: `Thalheim an der Thur` },
		{id: 159, name: `Uetikon am See` },
		{id: 227, name: `Seuzach` },
		{id: 248, name: `Uitikon` },
		{id: 2, name: `Affoltern am Albis` },
		{id: 244, name: `Geroldswil` },
		{id: 89, name: `Niederglatt` },
		{id: 141, name: `Thalwil` },
		{id: 68, name: `Rorbas` },
		{id: 224, name: `Pfungen` },
		{id: 251, name: `Weiningen (ZH)` },
		{id: 112, name: `Bubikon` },
		{id: 223, name: `Neftenbach` },
		{id: 9, name: `Mettmenstetten` },
		{id: 94, name: `Otelfingen` },
		{id: 29, name: `Flurlingen` },
		{id: 100, name: `Stadel` },
		{id: 116, name: `Grüningen` },
		{id: 31, name: `Henggart` },
		{id: 25, name: `Dachsen` },
		{id: 3, name: `Bonstetten` },
		{id: 51, name: `Bachenbülach` }
	];

	let rooms;
	let area;
	let price = '...'
	let selected;
	function handleSubmit() {
		let url =
            base_url +
            "/api/predict?bfs_number=" +
            selected.id +
            "&area=" +
            area +
            "&rooms=" +
            rooms;
        console.log(url);
        axios.get(url).then((response) => {
            price = 'CHF ' + response.data;
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
<div class="container text-center">

	<h1>Are you paying to much? Our model predicts that you should be paying {price}</h1>

	<div class="row justify-content-md-center">
	  <div class="col col-lg-2">
		<input type="number" class="form-control" placeholder="area" aria-label="area" bind:value={area}>
	  </div>
	  <div class="col col-lg-2">
		<input type="number" class="form-control" placeholder="rooms" aria-label="rooms" bind:value={rooms}>
	  </div>
	  <div class="col col-lg-2">

		<select bind:value={selected}>
			{#each bfs_number_names as bfs}
				<option value={bfs}>
					{bfs.name}
				</option>
			{/each}
		</select>
	  </div>
	  <div class="col-md-auto">
		<button type="button" class="btn btn-primary" on:click={handleSubmit}>price estimation</button>
	  </div>
	</div>
  </div>
