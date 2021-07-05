<template>
    <div class="page-sign-up">
        <div class="columns">
            <div class="column is-4 is-offset-4">
                <h1 class="title">Registrarse</h1>

                <form @submit.prevent="submitForm">
                    <div class="field">
                        <label>Nombre de Usuario</label>
                        <div class="control">
                            <input type="text" class="input" v-model="username">
                        </div>
                    </div>

                    <div class="field">
                        <label>Contraseña</label>
                        <div class="control">
                            <input type="password" class="input" v-model="password">
                        </div>
                    </div>

                    <div class="field">
                        <label>Repetir contraseña</label>
                        <div class="control">
                            <input type="password" class="input" v-model="password2">
                        </div>
                    </div>

                    <div class="notification is-danger" v-if="errors.length">
                        <p v-for="error in errors" v-bind:key="error">{{ error }}</p>
                    </div>

                    <div class="field">
                        <div class="control">
                            <button class="button is-dark">Registrarse</button>
                        </div>
                    </div>

                    <hr>

                    O <router-link to="/log-in">Clickea aqui</router-link> para iniciar sesion!
                </form>
            </div>
        </div>
    </div>
</template>

<script
    src="../store/SignUp">
</script>