<script>
    // Ein Array von Monaten und deren Farben
    const months = [
      { name: "Januar", color: "#FFDDDD" },
      { name: "Februar", color: "#FFEECC" },
      { name: "März", color: "#DDFFDD" },
      { name: "April", color: "#CCFFEE" },
      { name: "Mai", color: "#CCDDFF" },
      { name: "Juni", color: "#EEDDFF" },
      { name: "Juli", color: "#FFCCDD" },
      { name: "August", color: "#DDEEFF" },
      { name: "September", color: "#CCFFDD" },
      { name: "Oktober", color: "#FFDDCC" },
      { name: "November", color: "#EEDDCC" },
      { name: "Dezember", color: "#DDFFEE" }
    ];
  </script>
  
  <style>
    .calendar {
      display: grid;
      grid-template-columns: repeat(12, 1fr);
      gap: 16px;
      padding: 16px;
    }
    
    .month {
      display: flex;
      align-items: center;
      justify-content: center;
      height: 100px;
      border-radius: 6px;
      color: #333;
      font-size: 10px;
      font-weight: bold;
    }
  </style>
  
  <div class="calendar">
    {#each months as { name, color }}
      <div class="month" style="background-color: {color};">
        {name}
      </div>
    {/each}
  </div>

<!-- 
  Benutung in Code:
  <script>
    import Calendar from './Calendar.svelte';
  </script>
  
  <Calendar />
   -->