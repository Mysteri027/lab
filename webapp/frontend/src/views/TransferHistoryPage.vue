<template>
    <main class="lk-main">
        <div class="lk">
            <div class="lk-user">
                <div class="lk-container">
                    <h3 class="mb-5">Перевод на сумму <span class="badge bg-secondary">100500руб.</span> пользователю
                        <span class="badge bg-secondary">+7(800)555-35-35.</span></h3>
                    <h3 class="mb-5">Перевод на сумму <span class="badge bg-secondary">100500руб.</span> пользователю
                        <span class="badge bg-secondary">+7(800)555-35-35.</span></h3>
                    <h3 class="mb-5">Перевод на сумму <span class="badge bg-secondary">100500руб.</span> пользователю
                        <span class="badge bg-secondary">+7(800)555-35-35.</span></h3>
                </div>

            </div>
        </div>
    </main>
</template>

<style scoped>
.lk-main {
    display: table;
    position: absolute;
    top: 0;
    left: 0;
    height: 100%;
    width: 100%;
}

.lk {
    display: table-cell;
    vertical-align: middle;
}

.lk-user {
    margin-left: auto;
    margin-right: auto;
    width: 50%;
    height: 600px;
    display: flex;
}

.lk-container {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-content: center;
}
</style>

<script>
export default {
    name: "TransferHistoryPage"
}
</script>
