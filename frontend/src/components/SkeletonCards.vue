<template>
  <div class="cards">
      <div v-for="n in 3" :key="n" class="skeleton-card">
        <div class="skeleton-card-title" style="margin-bottom: 0.5em; width: 100%"></div>
        <div class="skeleton-card-title"></div>
        <div class="skeleton-card-subtitle"></div>
        <div class="skeleton-card-content" style="margin-top: 1.2em"></div>
        <div class="skeleton-card-content" style="width:80%"></div>
        <div class="skeleton-card-content"></div>
        <div class="skeleton-card-content"></div>

        <div class="skeleton-button"></div>
      </div>
  </div>
</template>

<script>
export default {

}
</script>

<style lang="scss" scoped>

//Variables
$dark: #282a2c;
$lightdark: lighten($dark, 5);
$white: whitesmoke;
$border-radius: 20px;

$primary: #9161cf;

.skeleton-card{
  background-color: $lightdark;
  padding: 2em;
  border-radius: $border-radius;
  margin-bottom: 1em;

  position: relative;
  overflow: hidden;

  z-index: -2;

  &::before{
    z-index: -1;
    content: '';
    position: absolute;
    left: 0;
    top: 0;
    // width: 20%;
    // filter: blur(8px);
    height: 100%;
    background-color: lighten($lightdark, 10);

    animation: skeleton-wipe infinite 1s ease;
  }

  .skeleton-card-title{
    width: 80%;
    height: 1.4em;
    background-color: $dark;
  }

  .skeleton-card-subtitle{
    margin-top: 1em;
    width: 80%;
    height: 1.2em;
    background-color: lighten($dark, 2);
  }

  .skeleton-card-content{
    margin-top: 0.8em;
    width: 100%;
    height: 1em;
    background-color: lighten($dark, 10);
  }

  .skeleton-button{
    margin-top: 2em;
    border-radius: 20px;
    width: 6em;
    height: 2.4em;
    background-color: $dark;
  }
}

@keyframes skeleton-wipe{
  from{
    left: 0;
    width: 30%;
  }
  to{
    width: 35%;
    left: 100%
  }
}

</style>