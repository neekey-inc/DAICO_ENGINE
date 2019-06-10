<template>
  <main class="container my-5">
    <div class="row">
      <div class="col-12 text-center my-3">
        <h2 class="mb-3 display-4 text-uppercase">{{ article.title }}</h2>
      </div>
      <!-- <div class="col-md-6 mb-4">
        <img
          v-if="!preview"
          class="img-fluid"
          style="width: 400px; border-radius: 10px; box-shadow: 0 1rem 1rem rgba(0,0,0,.7);"
          :src="article.image"
        >
        <img
          v-else
          class="img-fluid"
          style="width: 400px; border-radius: 10px; box-shadow: 0 1rem 1rem rgba(0,0,0,.7);"
          :src="preview"
        >
      </div> -->
      <div class="col-md-4">
        <form @submit.prevent="submitArticle">
          <div class="form-group">
            <label for>変更タイトル</label>
            <input type="text" class="form-control" v-model="article.title">
          </div>
          <div class="form-group">
            <label for>変更サムネ</label>
            <input type="file" @change="onFileChange">
          </div>
          <div class="row">
            <div class="col-md-6">
              <div class="form-group">
                <label for>カテゴリ</label>
                <select v-model="article.category" class="form-control">
                  <option value=1>家事代行</option>
                  <option value=2>育児代行</option>
                  <option value=3>掃除代行</option>
                  <option value=4>お墓参り代行</option>
                  <option value=5>買い物代行</option>
                  <option value=6>叱り代行</option>
                  <option value=7>謝罪代行</option>
                  <option value=8>並び代行</option>
                  <option value=9>出席代行</option>
                </select>
              </div>
            </div>
            <div class="col-md-6">
              <div class="form-group">
                <label for>
                  投稿日
                </label>
                <input v-model="article.date" type="date" class="form-control">
              </div>
            </div>
          </div>
          <div class="form-group mb-3">
            <label for>本文</label>
            <textarea v-model="article.text" class="form-control" rows="8"></textarea>
          </div>
          <button type="submit" class="btn btn-success">保存</button>
        </form>
      </div>
    </div>
  </main>
</template>
<script>
export default {
  head() {
    return {
      title: "Edit Article"
    };
  },
  async asyncData({ $axios, params }) {
    try {
      let article= await $axios.$get(`article/${params.id}`);
      return { article };
    } catch (e) {
      return { article: [] };
    }
  },
  data() {
    return {
      article: {
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
      this.article.image = files[0];
      this.createImage(files[0]);
    },
    createImage(file) {
      let reader = new FileReader();
      let vm = this;
      reader.onload = e => {
        vm.preview = e.target.result;
      };
      reader.readAsDataURL(file);
    },
    async submitArticle() {
      let editedArticle = this.article;
      // if (editedArticle.image.indexOf("http://") != -1) {
      //   delete editedArticle["image"];
      // }
      const config = {
        headers: { "content-type": "multipart/form-data" }
      };
      let formData = new FormData();
      for (let data in editedArticle) {
        formData.append(data, editedArticle[data]);
      }
      try {
        let response = await this.$axios.$patch(
          `article/${editedArticle.id}/`,
          formData,
          config
        );
        this.$router.push({name:'article'});
      } catch (e) {
        console.log(e);
      }
    }
  }
};
</script>

<style>
</style>
