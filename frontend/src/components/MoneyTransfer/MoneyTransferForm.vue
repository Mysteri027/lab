<template>
  <div class="lk-main">
    <div class="lk">
      <div class="lk-user">
        <div class="lk-container">
          <form class="input-form">
            <div class="mb-3">
              <label for="exampleFormControlInput1" class="form-label">Введите номер телефона</label>
              <phone-mask-input
                autoDetectCountry
                showFlag
                @onValidate="onValidate"
                wrapperClass="wrraper-example"
                inputClass="exampleFormControlInput1"
                flagClass="flag-example"
              />
            </div>
            <div class="mb-3">
              <label for="exampleFormControlInput2" class="form-label">Введите сумму перевода</label>
              <input type="number" class="form-control" id="exampleFormControlInput2">
            </div>
            <button class="btn btn-dark">Перевести</button>
          </form>
        </div>
      </div>
    </div>
  </div>
</template>

<script>

import PhoneMaskInput from  "vue-phone-mask-input";
export default {
  name: "MoneyTransferForm",
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
}

</style>