<template>
    <div class="page-success">
        <div class="columns is-multiline">
            <div class="column is-12">
                <h1 class="title">Muchas gracias</h1>

                <p>Su asiento será enviado en unos instantes a su correo</p>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: 'Success',
    mounted() {
        document.title = 'Aprobado | Djackets'
    },
}
</script>