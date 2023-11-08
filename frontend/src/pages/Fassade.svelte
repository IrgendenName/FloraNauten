<script>
  import { onMount } from "svelte";
  import axios from "axios";

  let fassade = {
    name: "Fassadenbegrünung",
    beschreibung: `Sie möchten Ihre Fassade begrünen. Das ist eine gute Idee. Die Begrünung Ihrer Fassade bringt vielfältige Vorteile für Mensch und Natur. Sie erhöhen das Wohlbefinden von uns Menschen und leisten einen wichtigen Beitrag zur Biodiversität. Ausserdem absorbieren die Begrünungen Stickoxide sowie Feinstaub und leisten somit einen wichtigen Beitrag für saubere Luft. Für die meisten Pflanzen ist die Installation einer Rankenhilfe notwendig.`,
    spezifizierung: ``,
    text1: "Drahtseile für eine Fassade in der Länge von 15m",
    text11: "37 Stk. à CHF 50.-",
    text12: "(Drahtseile werden im Abstand von 40 cm an Fassade geschraubt)",
    kosten1: "CHF 1850",
    text2: "Kletterpflanze Waldrebe 37 Stk. à CHF 50.-",
    kosten2: "CHF 1850",
    totaltext: "Total Materialkosten",
    totalpreis: "CHF 3700",
  };
</script>

<main>
  <h1>Empfohlene Massnahmen</h1>
  <br /> <br /><br /> <br />
  <div class="massnahme">
    <img src="fassademassnahme.jpg" alt="Fassade" class="image" />
    <h3><b>{fassade.name}</b></h3>
    <br />
    <h3>Beschreibung</h3>
    <p class="beschreibung">{fassade.beschreibung}</p>
    <br />
    <h3>Kosten</h3>
    <table>
      <tr>
        <td
          >{fassade.text1}<br /><br />{fassade.text11}<br /><br
          />{fassade.text12}</td
        >
        <td>{fassade.kosten1}</td>
      </tr>
      <tr>
        <td>{fassade.text2}</td>
        <td>{fassade.kosten2}</td>
      </tr>
      <tr>
        <td><b>{fassade.totaltext}</b></td>
        <td><b>{fassade.totalpreis}</b></td>
      </tr>
    </table>
  </div>
</main>

<style>
  .image {
    width: 100%;
    max-width: 400px; /* Adjust the maximum width as needed */
    height: auto;
    display: block;
    margin: 0 auto;
  }

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
