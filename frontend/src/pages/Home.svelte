<script>
   import { onMount } from "svelte";
    import axios from "axios";


   
</script>

<main>
  <img
    src="https://www.zg.ch/behoerden/gemeinden/risch-rotkreuz/verwaltung/tiefbau-umwelt-sicherheit-1/copy_of_laerm/umwelt/biodiversitaet/ftw-simplelayout-textblock/@@images/fb1f43c6-f23e-4b67-a4ec-c5e0823d2677.jpeg"
    alt="Biodiversität"
  />

  <h1>WARUM BIODIVERSITÄT FÜR UNS WICHTIG IST</h1>
  <p>
    Die Biodiversität – die Vielfalt der Gene, Arten und Lebensräume – ist
    unsere Lebensgrundlage. In der Schweiz sind zurzeit die Hälfte der
    Lebensräume und ein Drittel aller Arten bedroht. Darüber hinaus ist der
    Erhalt der biologischen Vielfalt wichtig für Erfolge beim Klimaschutz. Wir
    haben uns ambitionierte Ziele im Rahmen unserer Klimastrategie gesetzt: Als
    gesellschaftliche Akteurin wollen wir menschlichen Fortschritt ermöglichen,
    indem wir schützen, was wirklich wichtig ist – und dazu gehört die
    Biodiversität.
  </p>
  <button class="cta-button"> VERBINDE DICH JETZT MIT DER NATUR </button>
</main>

<style>
  /* Hintergrundbild und Stil für die Seite */
  main {
    /* background-image: url("your-image-path.jpeg"); */
    background-size: cover;
    background-position: center;
    height: 100vh;
    display: flex;
    flex-direction: column;
    justify-content: center;
    text-align: center;
    color: black;
  }

  /* Stil für die Überschrift */
  h1, h2, h3, h4, h5, h6 {
    font-size: 3rem;
    margin-bottom: 2rem;
    font-family: 'Julius Sans One';
  }

 

  /* Stil für den Absatz */
  p {
    font-size: 1.25rem;
    margin-bottom: 2rem;
  }

  /* Stil für den Call-to-Action Button */
  .cta-button {
    padding: 1rem 2rem;
    background: green;
    color: white;
    border: none;
    border-radius: 5px;
    font-size: 1rem;
    cursor: pointer;
    transition: background-color 0.3s ease;
  }

  .cta-button:hover {
    background: darkgreen;
  }
</style>
