<template>
    <div class="min-h-screen bg-grey-900 text-white flex flex-col items-center justify-center p-4">
        <h1 class="text-3xl font-bold mb-4">AI Hair Replacement</h1>
        <FileUploader @processed="setResult" />
        <ResultDisplay v-if="result" :image="result" />
    </div>
</template>

<script>
import FileUploader from './componenets/FileUploader.vue'
import ResultDisplay from './components/ResultDisplay.vue'

export default {
    components: { FileUploader, ReaultDisplay },
    data() {
        return { result: null }
    },
    methods: {
        setResult(url) {
            this.result = url
        }
    }
}
</script>