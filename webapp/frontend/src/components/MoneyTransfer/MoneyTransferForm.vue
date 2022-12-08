<template>
  <div class="lk-main">
    <div class="lk">
      <div class="lk-user">
        <div class="lk-container">

          <form class="input-form" @submit="makeTransfer">

            <div v-if="(error !== null)">
              <h3 class="mb-5">Ошибка <span class="badge bg-secondary">{{ this.error }}</span></h3>
            </div>

            <div class="mb-3">
              <label for="exampleFormControlInput1" class="form-label">Введите номер телефона(начиная с 8)</label>
              <input type="number" class="form-control" id="exampleFormControlInput2" v-model="phoneNumber">
            </div>

            <div class="mb-3">
              <label for="exampleFormControlInput2" class="form-label">Введите сумму перевода </label>
              <input type="number" class="form-control" id="exampleFormControlInput2" v-model="money">
            </div>

            <button class="btn btn-dark" type="submit">Перевести</button>
          </form>

        </div>
      </div>
    </div>
  </div>
</template>

<script>

import PhoneMaskInput from "vue-phone-mask-input";

export default {
  name: "MoneyTransferForm",
  data() {
    return {
      phoneNumber: " ",
      money: " ",
      error: null
    }
  },

  methods: {
    makeTransfer(event) {
      this.error = null
      const userId = localStorage.getItem("user")
      this.$http.post('api/maketranfer/', JSON.stringify({
        userId: userId,
        phoneNumber: this.phoneNumber,
        money: this.money
      }))
        .then((response) => {
          if (response.data.error) {
            this.error = response.data.error
          }
        })
      event.preventDefault()
    }
  },
  components: {
    PhoneMaskInput
  }
}
</script>

<style scoped>

.lk-main {
  display: flex;
  position: absolute;
  top: 0;
  left: 0;
  height: 100%;
  width: 100%;
  justify-content: center;
  align-content: center;
}

.lk {
  justify-content: center;

}

.lk-user {
  margin-left: auto;
  margin-right: auto;
  width: 50%;
  height: 600px;
  display: flex;
  justify-content: center;
  align-content: center;
}

.lk-container {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-content: center;
}

.input-form {
  background-color: white;
  border-radius: 10px;
  padding: 50px;
  width: 600px;
}

</style>