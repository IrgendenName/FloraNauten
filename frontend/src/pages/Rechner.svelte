<script>
  // Hier könnten Sie Ihre JavaScript-Logik einfügen, zum Beispiel für das Handhaben von Formulardaten
  let strasse = '';
  let hausnummer = '';
  let plz = '';
  let ort = '';

  const handleSubmit = () => {
    // Logik, um das Formular zu verarbeiten
    console.log({ strasse, hausnummer, plz, ort });
  };
</script>



<form on:submit|preventDefault={handleSubmit}>
  <div class="form-group">
    <label for="strasse">Strasse</label>
    <input id="strasse" type="text" bind:value={strasse} placeholder="Bitte auswählen" />
  </div>
  
  <div class="form-group">
    <label for="hausnummer">Hausnummer</label>
    <input id="hausnummer" type="number" bind:value={hausnummer} placeholder="Hausnummer" />

  </div>
  
  <div class="form-group">
    <label for="plz">PLZ</label>
    <input id="plz" type="number" bind:value={plz} placeholder="Postleitzahl" />

  </div>
  
  <div class="form-group">
    <label for="ort">Ort</label>
    <input id="ort" type="text" bind:value={ort} placeholder="Ort" />

  </div>
  
  <button type="submit">WEITER</button>
</form>


<style>
  .form-group {
    margin-bottom: 1rem;
  }

  label {
    display: block;
    margin-bottom: 0.5rem;
  }

  input, select {
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
    background-color: #0000FF;
    color: white;
    cursor: pointer;
  }

  button:hover {
    background-color: #0000CC;
  }
</style>