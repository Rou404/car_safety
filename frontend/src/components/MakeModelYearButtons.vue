<template>
    <div class='bg-gray-800 border-b border-gray-600'>
        <form class="flex flex-row justify-center p-10" @submit.prevent="searchCars">
            <div class="basis-1/4 p-2">
                <select class="select select-primary select-lg w-full max-w-xs" v-model="make" id="make"
                    @change="fetchAvailableModels">
                    <option disabled value="">Select Make</option>
                    <option v-for="makeOption in availableMakes" :key="makeOption">
                        {{ makeOption['make'] }}
                    </option>
                </select>
            </div>
            <div class="basis-1/4 p-2">
                <select class="select select-primary select-lg w-full max-w-xs" v-model="model" id="model"
                    @change="fetchAvailableYears">
                    <option disabled value="">Select Model</option>
                    <option v-for="modelOption in availableModels" :key="modelOption">
                        {{ modelOption['model'] }}
                    </option>
                </select>
            </div>
            <div class="basis-1/4 p-2">
                <select class="select select-primary select-lg w-full max-w-xs" v-model="year" id="year">
                    <option disabled value="">Select Year</option>
                    <option v-for="yearOption in availableYears" :key="yearOption">
                        {{ yearOption['model_year'] }}
                    </option>
                </select>
            </div>
            <div class="basis-1/4 p-2">
                <button class="btn btn-primary btn-xs sm:btn-sm md:btn-md lg:btn-lg" type="submit">Search</button>

            </div>

        </form>
    </div>
</template>

<script>
export default {
    data() {
        return {
            make: "",
            model: "",
            year: "",
            availableMakes: [],
            availableModels: [],
            availableYears: [],
            vehicle_id: null,
            safety_ratings: [],
        };
    },
    mounted() {
        this.fetchAvailableMakes();
        this.fetchAvailableModels();
        this.fetchAvailableYears();
    },
    methods: {
        async fetchAvailableMakes() {
            try {
                const response = await this.$axios.get('http://127.0.0.1:8001/api/car-makes/', {
                    headers: {
                        Accept: 'application/json',
                    },
                });
                console.log(response)
                this.availableMakes = response.data;
            } catch (error) {
                console.error('Error fetching available makes', error);
            }
        },
        async fetchAvailableModels() {
            if (this.make) {
                try {
                    const response = await this.$axios.get(`http://127.0.0.1:8001/api/car-makes/${this.make}/car-models/`, {
                        headers: {
                            Accept: 'application/json',
                        },
                    });

                    this.availableModels = response.data;
                } catch (error) {
                    console.error('Error fetching available models', error);
                }
            } else {
                this.availableModels = [];
            }
        },
        async fetchAvailableYears() {
            if (this.make && this.model)
                try {
                    const response = await this.$axios.get(`http://127.0.0.1:8001/api/car-makes/${this.make}/car-models/${this.model}/model_year/`, {
                        headers: {
                            Accept: 'application/json',
                        },
                    });

                    this.availableYears = response.data;
                } catch (error) {
                    console.error('Error fetching available years', error);
                }
        },
        async searchCars() {
            if (this.make && this.model && this.year) {
                try {
                    const response = await this.$axios.get(`http://127.0.0.1:8001/api/car-makes/${this.make}/car-models/${this.model}/model_year/${this.year}/`, {
                        headers: {
                            Accept: 'application/json',
                        },
                    });
                    this.vehicle_id = response.data[0]['vehicle_id'];
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

                        this.safety_ratings = response.data.Results[0];
                        this.$emit('makeModelYearSelected', this.safety_ratings);
                        console.error(this.safety_ratings);

                    } catch (error) {
                        console.error('Error fetching available years', error);
                    }
            }
        },
    },
};
</script>

<style scoped></style>
