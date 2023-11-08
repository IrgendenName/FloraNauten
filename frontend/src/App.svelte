<script>
	import Router from "svelte-spa-router";
	import routes from "./routes";
</script>

<!-- This part is always displayed -->
<div class="container mt-3">
	<a href="/">
		<img class="img-fluid logo" alt="Logo" src="Logo.png" />
	</a>


  <!-- Here we load the page depending on the current 	URL -->
  <Router {routes} />
</div>

<style>
	.logo {
		width: 5%;
		height: auto;
		margin-bottom: 100px;
		float: right;
		position: absolute;
		top: 10px;
		right: 10px;
	}
</style>

