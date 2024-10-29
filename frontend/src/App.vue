<!-- App.vue -->

<template>
  <div id="app" class="flex flex-col min-h-screen">
    <NavBar></NavBar>
    <MakeModelYearButtons @makeModelYearSelected="updateSafetyRating"></MakeModelYearButtons>
    <VehicleInformationCard v-if="searchPerformed" :safety_ratings="safety_rating"></VehicleInformationCard>
    <div class="flex flex-col w-full lg:flex-row m-auto p-8">
      <div class="grid flex-grow  place-items-center">
        <LatestVehiclesCards></LatestVehiclesCards>
      </div>
      <div class="grid flex-grow place-items-center">
        <LatestVehiclesCards></LatestVehiclesCards>
      </div>
      <div class="grid flex-grow place-items-center">
        <LatestVehiclesCards></LatestVehiclesCards>
      </div>
    </div>
    <Footer></Footer>
  </div>
</template>

<script>
import NavBar from "./components/NavBar.vue";
import Footer from "./components/Footer.vue";
import MakeModelYearButtons from "./components/MakeModelYearButtons.vue";
import VehicleInformationCard from "./components/VehicleInformationCard.vue";
import LatestVehiclesCards from "./components/LatestVehiclesCards.vue";

export default {
  name: 'App',
  components: {
    NavBar,
    Footer,
    MakeModelYearButtons,
    VehicleInformationCard,
    LatestVehiclesCards
  },
  data() {
    return {
      safety_rating: [],
      searchPerformed: false,
    };
  },
  methods: {
    updateSafetyRating(safety_rating) {
      this.safety_rating = safety_rating;
      this.searchPerformed = true;
    },
  },
};
</script>
