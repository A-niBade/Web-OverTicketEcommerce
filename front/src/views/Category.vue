<template>
    <div class="page-category">
        <div class="columns is-multiline">
            <div class="column is-12">
                <h2 class="is-size-2 has-text-centered">{{ category.name }}</h2>
            </div>

            <ProductBox 
                v-for="product in category.products"
                v-bind:key="product.id"
                v-bind:product="product" />
        </div>
    </div>
</template>

<script
    src="../store/Category.js">
</script>