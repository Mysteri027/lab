<template>
    <div class="container">
        <footer class="py-3 my-4">
            <ul class="nav justify-content-center border-bottom pb-3 mb-3">

                <li class="nav-item">
                    <div class="nav-link px-2 text-muted">
                        <router-link to="/">
                            <p class="text-center text-muted"aria-current="page">Личный кабинет</p>
                        </router-link>
                    </div>
                </li>

                <li class="nav-item">
                    <div class="nav-link px-2 text-muted">
                        <router-link to="/moneytransfer">
                            <p class="text-center text-muted"aria-current="page">Перевод</p>
                        </router-link>
                    </div>
                </li>

                <li class="nav-item">
                    <div class="nav-link px-2 text-muted">
                        <router-link to="/transferhistory">
                            <p class="text-center text-muted"aria-current="page">История платежей</p>
                        </router-link>
                    </div>
                </li>
            </ul>
            <p class="text-center text-muted">© 2022 OnlineBank, Inc</p>
        </footer>
    </div>
</template>

<script>
export default {
    name: "Footer"
}
</script>

<style scoped>

footer {
    position: absolute;
    bottom: 0;
    max-width: 1200px;
    width: 100%;
    height: 60px;
    line-height: 60px;
}

a {
    text-decoration: none;
    text-decoration: black;
}

</style>