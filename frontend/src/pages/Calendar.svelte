<script>
  // Ein Array von Monaten und deren Farben
  const months = [
    { name: "Januar", color: "#DDDDDD" },
    { name: "Februar", color: "#DDDDDD" },
    { name: "März", color: "#CCFAC9" },
    { name: "April", color: "#CCFAC9" },
    { name: "Mai", color: "#CCFAC9" },
    { name: "Juni", color: "#CCFAC9" },
    { name: "Juli", color: "#CCFAC9" },
    { name: "August", color: "#00B050" },
    { name: "September", color: "#00B050" },
    { name: "Oktober", color: "#00B050" },
    { name: "November", color: "#DDDDDD" },
    { name: "Dezember", color: "#DDDDDD" },
  ];
</script>

  <div class="calendar">
    {#each months as { name, color }}
      <div class="month" style="background-color: {color};">
        {name}
      </div>
    {/each}
  </div>
    <div style="display: flex; align-items: center; text-align: center; justify-content: center;">
      <div class="square" style="width: 20px; height: 20px; background-color: #CCFAC9; border-radius: 6px;"/>
      <p style="padding-top:15px; text-align:center; margin-left: 10px; margin-right: 50px">Düngern, Bewässern, Pflegen</p>
    
      <div class="square" style="width: 20px; height: 20px; background-color: #00B050; border-radius: 6px;"/>
      <p style="padding-top:15px; margin-left: 10px;">Pflanzen</p>
    </div>

  
  



<!-- 
  Benutung in Code:
  <script>
    import Calendar from './Calendar.svelte';
  </script>
  
  <Calendar />
   -->

<style>
  .calendar {
    display: grid;
    grid-template-columns: repeat(12, 1fr);
    gap: 5px;
    padding: 16px;
  }

  .month {
    display: flex;
    align-items: center;
    justify-content: center;
    height: 50px;
    border-radius: 6px;
    color: #333;
    font-size: 10px;
    font-weight: bold;
  }
</style>
