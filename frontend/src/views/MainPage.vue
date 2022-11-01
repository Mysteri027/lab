<template>
  <div class="lk-main">
    <div class="lk">
      <div class="lk-user">
        <div class="lk-container">
          <h1>Всего на счете <span class="badge bg-secondary">100500руб.</span></h1>
          <h1>Номер телефона <span class="badge bg-secondary">+7(800)555-35-35</span></h1>
        </div>
      </div>
    </div>
  </div>
</template>

<script>

export default {
  name: "MainPage",
}
</script>

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

.btn{
  width: 100px;
  padding: 5px;
  margin-bottom: 10px;
}

</style>