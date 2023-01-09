<template>
  <main class="lk-main">
    <div class="lk">
      <div class="lk-user">


        <div class="lk-container" v-if="this.transfers !== null">
          <div v-for="transfer in transfers">
            <h3 class="mb-5">Перевод на сумму <span
              class="badge bg-secondary">{{ transfer.transferMoneyCount }}</span> пользователю
              <span class="badge bg-secondary">{{ transfer.user_to }}.</span></h3>
          </div>
        </div>

        <div v-if="this.transfers == null">
          <h3 class="mb-5">Вы не совершали переводов </h3>
        </div>
      </div>
    </div>
  </main>
</template>

<script>
export default {
  name: "TransferHistoryPage",
  data() {
    return {
      transfers: null
    }
  },

  mounted() {
    const userId = localStorage.getItem("user")
    this.$http.get("api/moneytranfer/" + userId)
      .then(response => (
        this.transfers = this.checkResponse(response.data.items)
      ))
  },

  methods: {
    checkResponse(response) {
      if (response === "Пользователь не совершал переводов") {
        return null
      }
      return response
    }
  }
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
</style>
