<script>
  import { onMount } from "svelte";
  import axios from "axios";
  import Calendar from './Calendar.svelte';

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

  async function shareRecipe() {
    if (navigator.share) {
      try {
        await navigator.share({
          title: fassade.name, 
          text: "Schau dir diese Empfohlene Massnahme an:",
          url: `/fassade`, // Adjust the URL as needed
        });
        console.log(
          "Empfohlene Massnahme erfolgreich geteilt. Login erforderlich für Empfänger."
        );
      } catch (err) {
        console.error("Fehler beim Teilen:", err);
      }
    } else {
      alert("Die Web Share API wird von Ihrem Browser nicht unterstützt.");
    }
  }




</script>

<main>
    <div class="massnahme">
      <h1>Empfohlene Massnahmen</h1>
      <img src="fassademassnahme.jpg" alt="Fassade" class="image"/>
      <br/>
      
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
      <br/>
      <h3>Pflege</h3>
      <Calendar/>

      <button class="cta-button" style="margin-top: 50px;" on:click={shareRecipe}>Download PDF</button>

    </div>  

</main>

<style>
  .image {
    width: 100%;
    max-width: 600px; 
    height: auto;
    display: block;
    margin: 0 auto;
    margin-top: 50px;
    padding-bottom: 30px;
    padding-top: 10px
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

  h1 {margin-top: 140px;
  }

  .massnahme {
    max-width: 800px;
    margin: 10px;
    padding-top: 47%;
    padding-bottom: 100px;
  }

  h2 {
    margin-bottom: 10px;
  }

  h3 {
    margin-top: 20px;
  }

  .beschreibung {
    padding-top: 10px;
    margin: 10px;
  }

  table {
    width: 100%;
    border-collapse: collapse;
    margin-top: 20px;
  }

  th,
  td {
    border: 1px solid #a4a4a4;
    padding: 8px;
    text-align: left;
  }

  th {
    background-color: #f2f2f2;
  }
  /* Stil für den Call-to-Action Button */
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
</style>
