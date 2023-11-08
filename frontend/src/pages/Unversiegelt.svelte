<script>
  import { onMount } from "svelte";
  import axios from "axios";

  let unversiegelt = {
    name: "Begrünte Verkehrsfläche",
    beschreibung: `Ihre Fläche ist unversiegelt - das sind gute Voraussetzungen. Denn diese Flächen sind sickerfähig und bieten Pflanzen und Tieren Zugang zum Boden. Im Gegensatz zu versiegelten Flächen, welche für viele
Lebewesen eine Barriere darstellen, bilden unversiegelte Flächen wichtige Vernetzungselemente zwischen naturnahen Lebensräumen. Wichtig auch: Unversiegelte Flächen heizen sich im Sommer weniger auf, was auch dem Menschen zugutekommt.
`,
    material1:
      "Kiesfläche (Mergelbelag) für eine Verkehrsfläche von 40 Quadratmeter",
    anzahl1: "40",
    preis1: "CHF 38.-",
    total1: "CHF 1'520.-",
    material2: "Total Materialkosten",
    total2: "CHF 1'520.-",
  };
</script>

<main>
  <h1>Empfohlene Massnahmen</h1>
  <br /> <br /><br /> <br />
  <div class="massnahme">
    <h3><b>{unversiegelt.name}</b></h3>
    <br />
    <h3>Beschreibung</h3>
    <p class="beschreibung">{unversiegelt.beschreibung}</p>
    <br />
    <h3>Kosten</h3>
    <table>
      <thead>
        <tr>
          <th>Material</th>
          <th>Anzahl</th>
          <th>Preis / m2</th>
          <th>Total</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>{unversiegelt.material1}</td>
          <td>{unversiegelt.anzahl1}</td>
          <td>{unversiegelt.preis1}</td>
          <td>{unversiegelt.total1}</td>
        </tr>
        <tr>
          <td><b>{unversiegelt.material2}</b></td>
          <td />
          <td />
          <td><b>{unversiegelt.total2}</b></td>
        </tr>
      </tbody>
    </table>
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

  h1,
  h2,
  h3,
  h4,
  h5,
  h6 {
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
  }

  table {
    width: 100%;
    border-collapse: collapse;
    margin-top: 20px;
  }

  th,
  td {
    border: 1px solid #ddd;
    padding: 8px;
    text-align: left;
  }

  th {
    background-color: #f2f2f2;
  }
</style>
