<template>
    <div class="mb-6">
        <input type="file" @change="handleFile" accept="image/*" class="block mb-2" />
        <button @click="upload" class="bg-blue-600 px-4 py-2 rounded">Upload</button>
    </div>
</template>

<script>
export default {
    emits: ['processed'],
    data() {
        return { file: null }
    },
    methods: {
        handleFile(e) {
            this.file = e.target.files[0]
        },
        async upload() {
            const form = new FormData()
            form.append("file", this.file)

            const res = await fetch("http://localhost:8000/process-image/", {
                method: "POST",
                body: form
            })

            const data = await res.json()
            this.$emit("processed", data.result_url)
        }
    }
}
</script>