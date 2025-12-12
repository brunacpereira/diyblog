<template>

</template>

<script setup lang="ts">
    import { ref } from 'vue'
    import { IconArticle, IconDotsVertical } from '@tabler/icons-vue'
    import { RouterLink, useRoute } from 'vue-router'
    import type { Blog } from '@/types'

    const url = ref('/blogs/')

    const data = ref<Blog>()

</script>

<style>

</style>