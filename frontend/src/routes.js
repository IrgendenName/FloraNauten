// Pages
import Appartment from "./pages/Appartment.svelte";
import DrawClassification from "./pages/Draw.svelte";

export default {
    // Home
    '/': Appartment,
    '/appartment': Appartment,

    // Doku
    '/draw': DrawClassification,
}