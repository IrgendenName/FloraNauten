<script>
</script>

<main>
  <video src="images/flowers4.mp4" muted autoplay loop></video>

  <div class="overlay">
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
    <a class="nav-link" href="#/rechner">
      <button class="cta-button">VERBINDE DICH JETZT MIT DER NATUR </button>
    </a>
  </div>
</main>

<style>
  main video{
    width: 100vw;
    height: 100vh;
    object-fit: cover;
    position: fixed;
    left: 0;
    right: 0;
    top: 0;
    bottom: 0;
    z-index: -1;
  }

  .overlay{
    position: fixed;
    bottom: 5vh;
  }

  /* Stil für die Überschrift */
  h1, h2, h3, h4, h5, h6 {
    color: #fff;
    font-size: 3rem;
    margin-bottom: 2rem;
    margin-top: 30vh;
    font-family: 'Julius Sans One';

  }

  /* Stil für den Absatz */
  p {
    color: #fff;
    font-size: 1.0rem;
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
