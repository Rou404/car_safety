<template>
    <div class="flex  bg-gray-800 rounded-md overflow-hidden shadow-md border-t border-gray-600 text-white">
        <!-- Vehicle Image on the left -->
        <img :src="safety_ratings.VehiclePicture" alt="Vehicle Image"
            class="w-1/2 h-auto object-contain py-1 border-r border-gray-600" />

        <!-- Information on the right -->
        <div class="w-3/5 p-6">
            <h2 class="text-3xl font-semibold">{{ safety_ratings.Make }} {{ safety_ratings.Model }}</h2>
            <p class="text-sm text-gray-400">{{ safety_ratings.ModelYear }}</p>

            <!-- Overall Ratings -->
            <div class="mt-6">
                <h3 class="text-lg font-semibold mb-2">Overall Ratings</h3>
                <div v-for="(value, property) in overall_ratings" :key="property"
                    class="flex justify-between items-center py-1 border-b border-gray-600">
                    <span>{{ formatLabel(property) }}</span>
                    <span class="font-semibold">{{ value }}</span>
                </div>
            </div>

            <!-- Crash Test Ratings -->
            <div class="mt-6">
                <h3 class="text-lg font-semibold mb-2">Crash Test Ratings</h3>
                <div v-for="(value, property) in crash_test_ratings" :key="property"
                    class="flex justify-between items-center py-1 border-b border-gray-600">
                    <span>{{ formatLabel(property) }}</span>
                    <span class="font-semibold">{{ value }}</span>
                </div>
            </div>

            <!-- Electronic Safety Features -->
            <div class="mt-6">
                <h3 class="text-lg font-semibold mb-2">Electronic Safety Features</h3>
                <div v-for="(value, property) in electronic_safety_features" :key="property"
                    class="flex justify-between items-center py-1 border-b border-gray-600">
                    <span>{{ formatLabel(property) }}</span>
                    <span class="font-semibold">{{ value }}</span>
                </div>
            </div>

            <!-- Rollover Information -->
            <div class="mt-6">
                <h3 class="text-lg font-semibold mb-2">Rollover Information</h3>
                <div v-for="(value, property) in rollover_info" :key="property"
                    class="flex justify-between items-center py-1 border-b border-gray-600">
                    <span>{{ formatLabel(property) }}</span>
                    <span class="font-semibold">{{ value }}</span>
                </div>
            </div>

            <!-- Other Information -->
            <div class="mt-6">
                <h3 class="text-lg font-semibold mb-2">Other Information</h3>
                <div v-for="(value, property) in other_information" :key="property"
                    class="flex justify-between items-center py-1 border-b border-gray-600">
                    <span>{{ formatLabel(property) }}</span>
                    <span class="font-semibold">{{ value }}</span>
                </div>
            </div>
        </div>
    </div>
</template>


<script>
export default {
    props: {
        safety_ratings: {
            type: Object,
            default: () => ({}),
        },
    },
    computed: {
        overall_ratings() {
            const overall_ratings = [
                'OverallRating',
                'OverallFrontCrashRating',
                'OverallSideCrashRating',
                'sideBarrierRating-Overall'];

            return Object.fromEntries(
                Object.entries(this.safety_ratings)
                    .filter(([property]) => overall_ratings.includes(property))
            );
        },
        crash_test_ratings() {
            const crash_test_ratings = [
                'FrontCrashDriversideRating',
                'FrontCrashPassengersideRating',
                'SideCrashDriversideRating',
                'SideCrashPassengersideRating',
                'SidePoleCrashRating',
                'combinedSideBarrierAndPoleRating-Front',
                'combinedSideBarrierAndPoleRating-Rear'
            ];

            return Object.fromEntries(
                Object.entries(this.safety_ratings)
                    .filter(([property]) => crash_test_ratings.includes(property))
            );

        },
        electronic_safety_features() {
            const electronic_safety_features = [
                'NHTSAElectronicStabilityControl',
                'NHTSAForwardCollisionWarning',
                'NHTSALaneDepartureWarning'
            ];

            return Object.fromEntries(
                Object.entries(this.safety_ratings)
                    .filter(([property]) => electronic_safety_features.includes(property))
            );
        },
        other_information() {
            const other_information = [
                'RecallsCount',
                'InvestigationCount',
                'dynamicTipResult'
            ];

            return Object.fromEntries(
                Object.entries(this.safety_ratings)
                    .filter(([property]) => other_information.includes(property))
            );
        },
        rollover_info() {
            const rollover_info = ['RolloverPossibility', 'RolloverPossibility2', 'RolloverRating', 'RolloverRating2'];

            return Object.fromEntries(
                Object.entries(this.safety_ratings)
                    .filter(([property]) => rollover_info.includes(property))
            );
        },

    },
    methods: {
        formatLabel(property) {
            return property.replace(/([a-z])([A-Z])/g, '$1 $2').toUpperCase();
        },
    },
};
</script>

<style scoped></style>
