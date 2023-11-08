<script>
</script>

<main>
  <video src="images/flowers4.mp4" muted autoplay loop></video>

  <div class="overlay">

    <h1>BAUEN FÜR DIE NATUR<br/>SO FÖRDERN SIE DIE BIODIVERSITÄT</h1> <br/>
    <a class="nav-link" href="#/rechner">
      <button class="cta-button">JETZT ENTDECKEN</button>
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
    bottom: 5vh;
    justify-content: center;
    align-items: center;
    text-align: center;
    margin-top: 700px;
  }

  /* Stil für die Überschrift */
  h1, h2, h3, h4, h5, h6 {
    color: #fff;
    font-size: 3rem;
    margin-top: 30vh;
    font-family: 'Julius Sans One';

  }

  /* Stil für den Absatz */
  p {
    color: #fff;
    font-size: 1.0rem;
    margin-bottom: 2rem;
  }

  .nav-link{
    text-align: center;
  }
  /* Stil für den Call-to-Action Button */
  .cta-button {
    padding: 1rem 2rem;
    color: white;
    background: transparent;
    border: 3px solid white;
    font-size: 1rem;
    cursor: pointer;
    transition: background-color 0.3s ease;
  }

  .cta-button:hover {
    background: rgba(255,255,255, 0.3);
  }
</style>
