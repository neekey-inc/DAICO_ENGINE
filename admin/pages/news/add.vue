<template>
  <main class="container my-5">
    <div class="row">
      <div class="col-12 text-center my-3">
        <h2 class="mb-3 display-4 text-uppercase">{{ news.title }}</h2>
      </div>
      <!-- <div class="col-md-6 mb-4">
        <img
          v-if="preview"
          class="img-fluid"
          style="width: 400px; border-radius: 10px; box-shadow: 0 1rem 1rem rgba(0,0,0,.7);"
          :src="preview"
          alt
        >
        <img
          v-else
          class="img-fluid"
          style="width: 400px; border-radius: 10px; box-shadow: 0 1rem 1rem rgba(0,0,0,.7);"
          src="@/static/images/placeholder.png"
        >
      </div> -->
      <div class="col-md-4">
        <form @submit.prevent="submitNews">
          <div class="form-group">
            <label for>タイトル</label>
            <input type="text" class="form-control" v-model="news.title">
          </div>
          <div class="form-group">
            <label for>サムネ</label>
            <input type="file" name="file" @change="onFileChange">
          </div>
          <div class="row">
            <div class="col-md-6">
              <div class="form-group">
                <label for>カテゴリ</label>
                <select v-model="news.category" class="form-control">
                  <option value=1>代行エンジン</option>
                  <option value=2>キャンペーン</option>
                  <option value=3>特集</option>
                  <option value=4>お知らせ</option>
                </select>
              </div>
            </div>
            <div class="col-md-6">
              <div class="form-group">
                <label for>
                  投稿日
                </label>
                <input v-model="news.date" type="date" class="form-control">
              </div>
            </div>
          </div>
          <div class="form-group mb-3">
            <label for>本文</label>
            <textarea v-model="news.text" class="form-control" rows="8"></textarea>
          </div>
          <button type="submit" class="btn btn-primary">投稿</button>
        </form>
      </div>
    </div>
  </main>
</template>
<script>
  export default {
    head() {
      return {
        title: "Add News"
      };
    },
    data() {
      return {
        news: {
          title: "",
          image: "",
          category: "",
          date: null,
          text: ""
        },
        preview: ""
      };
    },
    methods: {
      onFileChange(e) {
        let files = e.target.files || e.dataTransfer.files;
        if (!files.length) {
          return;
        }
        this.news.image = files[0];
        this.createImage(files[0]);
      },
      createImage(file) {
        // let image = new Image();
        let reader = new FileReader();
        let vm = this;
        reader.onload = e => {
          vm.preview = e.target.result;
        };
        reader.readAsDataURL(file);
      },
      async submitNews() {
        const config = {
          headers: { "content-type": "multipart/form-data" }
        };
        let formData = new FormData();
        for (let data in this.news) {
          formData.append(data, this.news[data]);
        }
        try {
          let response = await this.$axios.$post("news/", formData, config);
          this.$router.push({name:'news'});
        } catch (e) {
          console.log(e);
        }
      }
    }
  };
</script>
<style>
</style>
