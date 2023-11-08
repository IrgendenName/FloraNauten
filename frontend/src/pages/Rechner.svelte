<script>
  let grundstueck = {
    gebaeude: 0,
    flaeche: 0,
    fassade: 0,
    balkon: 0,
    gruenflaeche: 0,
    verkehrsflaeche: 0,
    versiegelt: 0,
    unversiegelt: 0,
  };

  const handleImageClick = (property) => {
    grundstueck[property] = grundstueck[property] += 1;
  };

  let massnahme = {
    name: "",
    beschreibung: "",
    spezifizierung: "",
    kosten: 0,
  }

  function sendGrundstueckToServer() {
    axios.post("http://localhost:3001/api/massnahme/", grundstueck).then((response) => {
      massnahme = response.data;
    });
  }
</script>

<main>
  <h2>Um was für eine Fläche handelt es sich?</h2>

  <div class="text-center">
    <figure>
      <img
        src="gebaeude.png"
        alt="Gebäude"
        on:click={() => handleImageClick("gebaeude")}
      />
      <figcaption>Gebäude</figcaption>
    </figure>
    <figure>
      <img
        src="flaeche.png"
        alt="Fläche"
        on:click={() => handleImageClick("flaeche")}
      />
      <figcaption>Fläche</figcaption>
    </figure>
  </div>

  <br />

  {#if grundstueck.gebaeude === 1}
    <div class="text-center">
      <figure>
        <img
          src="fassade.jpg"
          alt="Fassade"
          on:click={() => handleImageClick("fassade")}
        />
        <figcaption>Fassade</figcaption>
      </figure>
      <figure>
        <img
          src="balkon.png"
          alt="Balkon"
          on:click={() => handleImageClick("balkon")}
        />
        <figcaption>Balkon</figcaption>
      </figure>
    </div>
  {/if}

  {#if grundstueck.flaeche === 1}
    <div class="text-center">
      <figure>
        <img
          src="gruenflaeche.png"
          alt="Grünfläche"
          on:click={() => handleImageClick("gruenflaeche")}
        />
        <figcaption>Grünfläche</figcaption>
      </figure>
      <figure>
        <img
          src="verkehrsflaeche.jpg"
          alt="Verkehrsfläche"
          on:click={() => handleImageClick("verkehrsflaeche")}
        />
        <figcaption>Verkehrsfläche</figcaption>
      </figure>
    </div>
    <br /><br />
    {#if grundstueck.verkehrsflaeche === 1}
      <div class="text-center">
        <figure>
          <img
            src="versiegelt.jpg"
            alt="Versiegelt"
            on:click={() => handleImageClick("versiegelt")}
          />
          <figcaption>Versiegelt</figcaption>
        </figure>
        <figure>
          <img
            src="unversiegelt.jpg"
            alt="Unversiegelt"
            on:click={() => handleImageClick("unversiegelt")}
          />
          <figcaption>Unversiegelt</figcaption>
        </figure>
      </div>
    {/if}
  {/if}


  <button onclick="sendGrundstueckToServer()">Massnahmen anzeigen</button>



<p>{massnahme.name}</p>
<p>{massnahme.beschreibung}</p>
<p>{massnahme.spezifizierung}</p>
<p>{massnahme.kosten}</p>



</main>

<style>
  main {
    display: flex;
    flex-direction: column;
    align-items: center;
    height: 100vh;
  }

  h1,
  h2,
  h3,
  h4,
  h5,
  h6 {
    font-size: 3rem;
    margin-bottom: 2rem;
    font-family: "Julius Sans One";
  }

  .form-group {
    margin-bottom: 1rem;
  }

  label {
    display: block;
    margin-bottom: 0.5rem;
  }

  input,
  select {
    width: 100%;
    padding: 0.5rem;
    margin-bottom: 0.5rem;
    border: 1px solid #ccc;
    border-radius: 4px;
  }

  button {
    padding: 0.5rem 1rem;
    border: none;
    border-radius: 4px;
    background-color: white;
    color: #010101;
    cursor: pointer;
    border: 1px solid lightgreen;
  }

  button:hover {
    background-color: lightgrey;
  }

  .text-center {
    display: flex;
    justify-content: center;
    align-items: center;
  }

  .text-center img {
    width: 5cm;
    height: 5cm;
    margin: 0.5cm;
    border: 2px solid transparent;
  }

  .text-center img:hover {
    border-color: gray;
  }

  figure {
    text-align: center;
  }

  figcaption {
    margin-top: 0.2rem;
    font-family: "Julius Sans One";
  }
</style>
