<script>
  import { onMount } from "svelte";
  import axios from "axios";

  let fassade = {
    name: "Fassade",
    beschreibung: "",
    spezifizierung: "",
    kosten: 0,
  };

  let gruenflaeche = {
    name: "Grünfläche",
    beschreibung: "",
    spezifizierung: "",
    kosten: 0,
  };

  let unversiegelt = {
    name: "Lorem ipsum",
    beschreibung: `Lorem ipsum dolor sit amet, consetetur sadipscing elitr, 
                    sed diam nonumy eirmod tempor invidunt ut labore et dolore 
                    magna aliquyam erat, sed diam voluptua. At vero eos et accusam 
                    et justo duo dolores et ea rebum. Stet clita kasd gubergren, 
                    no sea takimata sanctus est Lorem ipsum dolor sit amet. 
                    Lorem ipsum dolor sit amet, consetetur sadipscing elitr, 
                    sed diam nonumy eirmod tempor invidunt ut labore et dolore 
                    magna aliquyam erat, sed diam voluptua. At vero eos et accusam 
                    et justo duo dolores et ea rebum. Stet clita kasd gubergren, 
                    no sea takimata sanctus est Lorem ipsum dolor sit amet.`,
    spezifizierung: `Lorem ipsum dolor sit amet, consetetur sadipscing elitr, 
                      sed diam nonumy eirmod tempor invidunt ut labore et dolore 
                      magna aliquyam erat, sed diam voluptua. At vero eos et accusam 
                      et justo duo dolores et ea rebum. Stet clita kasd gubergren`,
    kosten: "CHF 25/m2",
  };
</script>

<main>
  <h1>Empfohlene Massnahmen</h1>
  <div class="massnahme">

    <h3>{unversiegelt.name}</h3>
    <br>
    <h3>Beschreibung</h3>
    <p class="beschreibung">{unversiegelt.beschreibung}</p>
    <br>
    <h3>Spezifizierung</h3>
    <p class="spezifizierung">{unversiegelt.spezifizierung}</p>
    <br><h3>Kosten</h3>
    <p class="kosten">Kosten: {unversiegelt.kosten}</p>
  </div>
</main>

<style>
  main {
    background-size: cover;
    background-position: center;
    height: 100vh;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    text-align: center;
    color: black;
  }

  h1, h2, h3, h4, h5, h6 {
  
    font-family: "Julius Sans One";
  }

  .massnahme {

    max-width: 600px;
    margin: 20px;
  }

  h2 {
    margin-bottom: 10px;
  }

  h3 {
    margin-top: 20px;
  }

  .beschreibung {
    margin-bottom: 10px;
    text-align: left;
  }

  .spezifizierung {
    font-size: 1rem;
    margin-bottom: 10px;
    text-align: left;
  }


</style>
