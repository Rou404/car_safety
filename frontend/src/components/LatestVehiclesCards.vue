<script>
export default {
    data() {
        return {
            safety_ratings: []
        };
    },
    mounted() {
        this.searchCars();
    },
    methods: {
        async fetchAvailableMakes() {
            try {
                const response = await this.$axios.get('http://127.0.0.1:8001/api/random/', {
                    headers: {
                        Accept: 'application/json',
                    },
                });

                this.availableMakes = response.data;
            } catch (error) {
                console.error('Error fetching available makes', error);
            }
        },
        async searchCars() {
            try {
                const response = await this.$axios.get(`http://127.0.0.1:8001/api/random/`, {
                    headers: {
                        Accept: 'application/json',
                    },
                });
                this.vehicle_id = response.data;
            } catch (error) {
                console.error('Error fetching available years', error);
            }
            if (this.vehicle_id)
                try {
                    const response = await this.$axios.get(`https://api.nhtsa.gov/SafetyRatings/VehicleId/${this.vehicle_id}/`, {
                        headers: {
                            Accept: 'application/json',
                        },
                    });
                    if (response.data.Results[0].VehiclePicture)
                        this.safety_ratings = response.data.Results[0];
                    else
                        this.searchCars()
                } catch (error) {
                    console.error('Error fetching available years', error);
                }
        }
    },

};



</script>

<template>
    <div class="card w-96 bg-base-300 shadow-xl">
        <figure> <img :src="safety_ratings.VehiclePicture" class="object-contain" alt="Vehicle Image"> </figure>
        <div class="card-body">
            <h2 class="card-title">{{ safety_ratings.Make }}</h2>
            <h2 class="card-subtitle py-1 border-y border-gray-600">{{ safety_ratings.Model }} {{ safety_ratings.ModelYear
            }}</h2>
            <p class="pb-1 border-b border-gray-600">Overall Rating {{ safety_ratings.OverallRating }}</p>
        </div>
    </div>
</template>

<style scoped></style>