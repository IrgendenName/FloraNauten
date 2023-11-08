<script>


let path = "";


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
    path = property;
  };

  let massnahme = {
    name: "",
    beschreibung: "",
    spezifizierung: "",
    kosten: 0,
  };

  // function sendGrundstueckToServer() {
  //   axios.post("http://localhost:3001/api/massnahme/", grundstueck).then((response) => {
  //     massnahme = response.data;
  //   });
  // }

  function sendGrundstueckToServer() {
    axios.post("http://localhost:3001/api/massnahme/", grundstueck).then(() => {
      // Navigate to Massnahmen.svelte and pass grundstueck data as a parameter
      goto("/Massnahmen", { grundstueck });
    });
  }
</script>

<main>
  <h2>wo möchten Sie Biodiversität fördern?</h2>

  <div class="text-center">
    <figure>
      <img
        src="gebaeude.png"
        alt="Gebäude"
        on:click={() => handleImageClick("gebaeude")}
        class:active={grundstueck.gebaeude === 1}

      />
      <figcaption>An einem Gebäude</figcaption>
    </figure>
    <figure>
      <img
        src="flaeche.png"
        alt="Fläche"
        on:click={() => handleImageClick("flaeche")}
        class:active={grundstueck.flaeche === 1}

      />
      <figcaption>Auf einer Fläche</figcaption>
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
          class:active={grundstueck.fassade === 1}

        />
        <figcaption>Fassade</figcaption>
      </figure>
      <figure>
        <img
          src="balkon.png"
          alt="Balkon"
          on:click={() => handleImageClick("balkon")}
          class:active={grundstueck.balkon === 1}

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
          class:active={grundstueck.gruenflaeche === 1}

        />
        <figcaption>Grünfläche</figcaption>
      </figure>
      <figure>
        <img
          src="verkehrsflaeche.jpg"
          alt="Verkehrsfläche"
          on:click={() => handleImageClick("verkehrsflaeche")}
          class:active={grundstueck.verkehrsflaeche === 1}

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
            class:active={grundstueck.versiegelt === 1}

          />
          <figcaption>Versiegelt</figcaption>
        </figure>
        <figure>
          <img
            src="unversiegelt.jpg"
            alt="Unversiegelt"
            on:click={() => handleImageClick("unversiegelt")}
            class:active={grundstueck.unversiegelt === 1}

          />
          <figcaption>Unversiegelt</figcaption>
        </figure>
      </div>
    {/if}
  {/if}

  <a href={"#/" + path}>
    <button class="cta-button">Massnahmen anzeigen</button>
  </a>

  <!-- <p>{massnahme.name}</p>
<p>{massnahme.beschreibung}</p>
<p>{massnahme.spezifizierung}</p>
<p>{massnahme.kosten}</p> -->
</main>

<style>
  .text-center img.active {
    border: 2px solid gray;
  }

  main {
    display: flex;
    flex-direction: column;
    align-items: center;
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

  .cta-button {
    padding: 1rem 2rem;
    color: black;
    background: transparent;
    border: 3px solid black;
    font-size: 1rem;
    cursor: pointer;
    transition: background-color 0.3s ease;
  }

  .cta-button:hover {
    background: rgba(0, 0, 0, 0.1);
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
