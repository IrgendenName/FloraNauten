<script>
  import { onMount } from "svelte";
  import axios from "axios";


  let fassade = {
    name: "fassade",
    beschreibung: "",
    spezifizierung: "",
    kosten: 0,
}

let gruenflaeche = {
    name: "gruenflaeche",
    beschreibung: "",
    spezifizierung: "",
    kosten: 0,
}

let unversiegelt = {
    name: "unversiegelt",
    beschreibung: "",
    spezifizierung: "",
    kosten: 0,
}





</script>

<main>
  <h1>Empfohlene Massnahmen</h1>
  <li>{unversiegelt.name}</li>
  <li>{fassade.name}</li>
  <li>{gruenflaeche.name}</li>





</main>

<style>
  main {
    background-size: cover;
    background-position: center;
    height: 100vh;
    display: flex;
    flex-direction: column;
    /* justify-content: center; */
    text-align: center;
    color: black;
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

  p {
    font-size: 1.25rem;
    margin-bottom: 2rem;
  }
</style>
