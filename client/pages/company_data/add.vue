<template>
  <main class="container my-5">
    <div class="row">
      <div class="col-12 text-center my-3">
        <h2 class="mb-3 display-4 text-uppercase">{{ company_data.name }}</h2>
      </div>
      <div class="col-md-4">
        <form @submit.prevent="submitCompany_data">
          <div class="form-group">
            <label for>会社名</label>
            <input type="text" class="form-control" v-model="company_data.name">
          </div>
          <div class="form-group">
            <label for>変更サムネ</label>
            <input type="file" @change="onFileChange">
          </div>
          <div class="row">
            <div class="col-md-6">
              <div class="form-group">
                <label for>カテゴリ</label>
                <select v-model="company_data.category" class="form-control">
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
          </div>
          <div class="row">
            <div class="form-group">
              <label for>PR文</label>
              <textarea v-model="company_data.pr" class="form-control" rows="8"></textarea>
            </div>
          </div>
          <div>
            <label>代表名</label>
            <input type="text" class="form-control" v-model="company_data.ceo">
          </div>
          <div>
            <label>電話番号</label>
            <input type="text" class="form-control" v-model="company_data.tell">
          </div>
          <div>
            <label>サービスの目玉・ポイント</label>
            <textarea v-model="company_data.point" class="form-control" rows="8"></textarea>
          </div>
          <div>
            <label>エリア(都道府県)</label>
            <input type="text" class="form-control" v-model="company_data.area1">
          </div>
          <div>
            <label>エリア(市町村)</label>
            <input type="text" class="form-control" v-model="company_data.area2">
          </div>
          <div>
            <label>料金</label>
            <input type="text" class="form-control" v-model="company_data.price">
          </div>
          <div>
            <label>本社住所</label>
            <input type="text" class="form-control" v-model="company_data.address">
          </div>
          <div>
            <label>創業年</label>
            <input type="text" class="form-control" v-model="company_data.year">
          </div>
          <div>
            <label>利用可能クレジットカード</label>
            <input type="text" class="form-control" v-model="company_data.cledit">
          </div>
          <div>
            <label>ホームページ</label>
            <input type="text" class="form-control" v-model="company_data.homepage">
          </div>
          <div>
            <label>社員数</label>
            <input type="text" class="form-control" v-model="company_data.staff">
          </div>
          <div>
            <label>サービスについて</label>
            <textarea v-model="company_data.service" class="form-control" rows="8"></textarea>
          </div>
          <div>
            <label>お支払いについて</label>
            <textarea v-model="company_data.pay" class="form-control" rows="8"></textarea>
          </div>
          <div>
            <label>キャンセルについて</label>
            <textarea v-model="company_data.cancel" class="form-control" rows="8"></textarea>
          </div>
          <div>
            <label>セキュリティー対策</label>
            <textarea v-model="company_data.security" class="form-control" rows="8"></textarea>
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
        name: "Add Company_data"
      };
    },
    data() {
      return {
        company_data: {
          name: "",
          image: "",
          category: "",
          // date: null,
          // text: ""
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
        this.company_data.image = files[0];
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
      async submitCompany_data() {
        const config = {
          headers: { "content-type": "multipart/form-data" }
        };
        let formData = new FormData();
        for (let data in this.company_data) {
          formData.append(data, this.company_data[data]);
        }
        try {
          let response = await this.$axios.$post("company_data/", formData, config);
          this.$router.push({name:'company_data'});
        } catch (e) {
          console.log(e);
        }
      }
    }
  };
</script>
<style>
</style>
