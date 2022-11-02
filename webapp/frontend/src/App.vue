<template>
    <div class="wrapper">
        <NavigationBar/>
        <router-view/>
        <Footer/>
    </div>
</template>

<style>
html, body {
    padding: 0;
    margin: 0;
    font-family: 'Open Sans', sans-serif;
}

.wrapper {
    min-height: 100vh;
    margin-bottom: 30px;
}

body {
    min-height: 100vh;
    position: relative;
    box-sizing: border-box;
  background-color: #edeef0;
}
.wrapper {
    min-height: 100vh;
    margin-bottom: 30px;
}

</style>

<script>

import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'

import NavigationBar from "@/components/NavigationBar";
import Footer from "@/components/Footer";

export default {
    name: 'App',
    components: {
        Footer,
        NavigationBar
    }
};
</script>
