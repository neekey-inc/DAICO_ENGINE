<template>
  <section>
    <el-button type="danger"><a @click="$router.push({name:'company_data-add'})">add 会社情報</a></el-button>
    <h3>会社情報</h3>
    <el-row>
      <el-col :span="6" v-for="company_data in company_datas" :key="company_data.id">
        <el-card :body-style="{ padding: '0px' }">
          <img :src="company_data.image" class="image">
          <div>{{company_data.name}}</div>
          <div>{{company_data.pr}}</div>
          <div>{{company_data.ceo}}</div>
          <div>{{company_data.tell}}</div>
          <div>{{company_data.point}}</div>
          <div>{{company_data.area1}}</div>
          <div>{{company_data.area2}}</div>
          <teble>
            <div>{{company_data.price}}</div>
            <div>{{company_data.address}}</div>
            <div>{{company_data.year}}年</div>
            <div>{{company_data.cledit}}</div>
            <div>{{company_data.homepage}}</div>
            <div>{{company_data.staff}}名</div>
            <div>{{company_data.service}}</div>
            <div>{{company_data.pay}}</div>
            <div>{{company_data.cancel}}</div>
            <div>{{company_data.security}}</div>
          </teble>
          <div style="padding: 14px;">
            <!-- <span><el-button type="primary">{{company_data.name}}</el-button></span> -->
            <span><a @click="$router.push({name:'company_data-edit', params:{id:company_data.id}})"><el-button type="warning">編集</el-button></a></span>
          </div>
        </el-card>
      </el-col>
    </el-row>
  </section>
</template>

<script>
  export default{
    data() {
      return {
        company_datas: [],
      }
    },
    mounted() {
      this.fetchData()
    },
    methods: {
      async fetchData() {
        let res = await this.$axios.$get('company_data/')
        this.company_datas = res
      },
    }
  }
</script>
<style>
  .recipe-card {
      box-shadow: 0 1rem 1.5rem rgba(0,0,0,.6);
  }
    .time {
    font-size: 13px;
    color: #999;
  }

  .bottom {
    margin-top: 13px;
    line-height: 12px;
  }

  .button {
    padding: 0;
    float: right;
  }

  .image {
    width: 100%;
    height: 200px;
    display: block;
  }

  .clearfix:before,
  .clearfix:after {
      display: table;
      content: "";
  }

  .clearfix:after {
      clear: both
  }
</style>

