<template>
  <el-container>
    <el-header>
      Header
      <a @click="$router.push({name:'pamphlet-company'})"><el-link type="primary">企業様へ</el-link></a>
      <a @click="$router.push({name:'pamphlet-service'})"><el-link type="primary">代行ENGINEとは</el-link></a>
      <el-row>
        <el-button><a @click="$router.push({name:'home'})">ロゴ</a></el-button>
        <el-button type="primary">カテゴリー一覧</el-button>
        <el-button type="warning">マイページ</el-button>
      </el-row>
    </el-header>
    <el-main>
      Main
      <h1>国内1000社以上の代行会社を検索・比較・予約ができるサイト！</h1>
      <h3><i class="el-icon-search"></i>カテゴリ一括検索 | <i class="el-icon-check"></i>簡単比較 | <i class="el-icon-thumb"></i>サイト内で予約完了</h3>
      <h1>news(特集、キャンペーン)</h1>
      <div class="block">
        <el-carousel trigger="click" height="150px">
          <el-carousel-item v-for="item in 4" :key="item">
            <h3 class="small">{{ item }}</h3>
          </el-carousel-item>
        </el-carousel>
      </div>
      <h1>カテゴリー</h1>
      <el-table
        :data="tableData"
        border
        style="width: 100%">
        <el-table-column
          prop="date"
          label="Category"
          width="180">
        </el-table-column>
        <el-table-column
          prop="name"
          label="Description"
          width="180">
        </el-table-column>
        <el-table-column
          prop="address"
          label="Price">
        </el-table-column>
      </el-table>
      <h1>口コミ</h1>
      <div class="reviewbox">
        <h3>name,age,srvice</h3>
        description
        <el-rate v-model="value1"></el-rate>
      </div>
      <h1>記事</h1>
      <div class="block">
        <el-carousel trigger="click" height="150px">
          <el-carousel-item v-for="item in 4" :key="item">
            <h3 class="small">{{ item }}</h3>
          </el-carousel-item>
        </el-carousel>
      </div>
    </el-main>
    <el-footer>
      Footer
      <div>
        ピックアップカテゴリー
        代行ENGINEについて
        企業向け
      </div>
      <div>
        Neekeyについて
        プライバシーポリシー
        利用規約
      </div>
      <footer>©Neekey.inc 2019-2020 allright reserved 無断転載禁止</footer>
    </el-footer>
  </el-container>
</template>

<script>
  export default {
  data() {
    return {
      tableData: [{
        date: '家事代行',
        name: 'あなたの代わりに家事を行います',
        address: '¥ 2500~5000'
      }, {
        date: '育児代行',
        name: 'あなたの代わりに家事を行います',
        address: '¥ 2500~5000'
      }, {
        date: '掃除代行',
        name: 'あなたの代わりに家事を行います',
        address: '¥ 2500~5000'
      }, {
        date: 'お墓参り代行',
        name: 'あなたの代わりに家事を行います',
        address: '¥ 2500~5000'
      }]
    }
  }
}
</script>

<style>
  .el-carousel__item h3 {
    color: #475669;
    font-size: 14px;
    opacity: 0.75;
    line-height: 150px;
    margin: 0;
  }

  .el-carousel__item:nth-child(2n) {
    background-color: #99a9bf;
  }

  .el-carousel__item:nth-child(2n+1) {
    background-color: #d3dce6;
  }

  .reviewbox {
    border: 1px solid #e8eaec;
  }
</style>
