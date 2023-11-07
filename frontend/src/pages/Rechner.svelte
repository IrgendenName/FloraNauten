<script>
  let grundstueck = {
    gebaeude: 0,
    gruenflaeche: 0,
    fassade: 0,
    balkon: 0,
  };

  const handleImageClick = (property) => {
    // Ändert den Wert der übergebenen Eigenschaft (z.B., 'gebaeude') von 1 auf 0 oder umgekehrt
    grundstueck[property] = grundstueck[property] === 1 ? 0 : 1;
  };
</script>

<img
  src="gebaeude.jpg"
  alt="Gebäude"
  on:click={() => handleImageClick("gebaeude")}
/>
<img
  src="gruenflaeche.jpg"
  alt="Grünfläche"
  on:click={() => handleImageClick("gruenflaeche")}
/>

<br>
{#if grundstueck.gebaeude === 1}
  <img src="fassade.jpg" alt="Fassade" />
  <img src="balkon.jpg" alt="Balkon" />
{/if}
{#if grundstueck.gruenflaeche === 1}
  <img src="gruenflaeche.jpg" alt="Grünfläche" />
{/if}

<style>
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

  img {
    width: 10%;
    height: auto;
    margin-bottom: 1rem;
  }
</style>
