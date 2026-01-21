<template>
    <div>
        <h2 class="text-xl mb-2">Processed Image</h2>
        <img :src="image" alt="Result" class="rounded shadow-lg" />
    </div>
</template>

<script>
exports default {
    props: ['image']
}
</script>