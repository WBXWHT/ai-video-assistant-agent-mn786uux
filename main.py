import json
import random
import datetime
from typing import List, Dict, Any

class VideoMaterial:
    """视频素材类，模拟素材库中的素材"""
    
    def __init__(self, material_id: str, category: str, tags: List[str], duration: int):
        self.id = material_id
        self.category = category  # 素材类别：风景、人物、产品等
        self.tags = tags          # 素材标签
        self.duration = duration  # 素材时长（秒）

class AIVideoAssistant:
    """AI视频剪辑助手核心类"""
    
    def __init__(self):
        # 初始化模拟素材库
        self.material_library = self._init_material_library()
        # 模拟AI模型的知识库（关键词到素材类别的映射）
        self.keyword_mapping = {
            "旅游": ["风景", "户外"],
            "产品": ["产品", "特写"],
            "人物": ["人物", "肖像"],
            "节日": ["庆祝", "人群"],
            "美食": ["食物", "烹饪"]
        }
    
    def _init_material_library(self) -> List[VideoMaterial]:
        """初始化模拟素材库"""
        materials = [
            VideoMaterial("MT001", "风景", ["自然", "山水", "旅游"], 10),
            VideoMaterial("MT002", "风景", ["城市", "建筑", "夜景"], 8),
            VideoMaterial("MT003", "产品", ["科技", "手机", "特写"], 5),
            VideoMaterial("MT004", "产品", ["家电", "家居", "展示"], 6),
            VideoMaterial("MT005", "人物", ["肖像", "商务", "微笑"], 7),
            VideoMaterial("MT006", "人物", ["团队", "合作", "办公"], 9),
            VideoMaterial("MT007", "美食", ["烹饪", "餐厅", "美味"], 8),
            VideoMaterial("MT008", "节日", ["庆祝", "派对", "欢乐"], 10),
        ]
        return materials
    
    def analyze_script(self, script: str) -> Dict[str, Any]:
        """分析用户文案，提取关键信息"""
        print(f"正在分析文案: {script[:50]}...")
        
        # 模拟AI分析过程
        detected_categories = []
        for keyword, categories in self.keyword_mapping.items():
            if keyword in script:
                detected_categories.extend(categories)
        
        # 去重
        detected_categories = list(set(detected_categories))
        
        # 如果没有检测到特定关键词，使用默认类别
        if not detected_categories:
            detected_categories = ["通用", "展示"]
        
        return {
            "script_length": len(script),
            "detected_categories": detected_categories,
            "estimated_video_duration": min(60, max(15, len(script) // 10))  # 根据文案长度估算视频时长
        }
    
    def match_materials(self, categories: List[str], max_duration: int) -> List[VideoMaterial]:
        """根据类别匹配素材"""
        matched_materials = []
        
        for material in self.material_library:
            # 检查素材类别是否匹配
            if material.category in categories:
                # 检查素材标签是否匹配（模拟AI的语义理解）
                for category in categories:
                    if any(tag in material.tags for tag in [category]):
                        matched_materials.append(material)
                        break
        
        # 随机选择素材（模拟AI的智能选择）
        if len(matched_materials) > 3:
            matched_materials = random.sample(matched_materials, 3)
        
        # 确保总时长不超过限制
        total_duration = sum(m.duration for m in matched_materials)
        while total_duration > max_duration and len(matched_materials) > 1:
            matched_materials.pop()
            total_duration = sum(m.duration for m in matched_materials)
        
        return matched_materials
    
    def generate_video_draft(self, script: str) -> Dict[str, Any]:
        """生成视频初稿"""
        print("=" * 50)
        print("AI智能视频剪辑助手开始工作...")
        print(f"处理时间: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        
        # 步骤1: 分析文案
        analysis_result = self.analyze_script(script)
        print(f"文案分析完成，检测到类别: {analysis_result['detected_categories']}")
        
        # 步骤2: 匹配素材
        matched_materials = self.match_materials(
            analysis_result['detected_categories'],
            analysis_result['estimated_video_duration']
        )
        print(f"素材匹配完成，找到 {len(matched_materials)} 个素材")
        
        # 步骤3: 生成视频结构
        video_structure = self._create_video_structure(script, matched_materials)
        
        # 计算效率提升（模拟数据）
        original_time = 120  # 假设原始制作时间120分钟
        ai_assisted_time = 72  # AI辅助后72分钟
        efficiency_improvement = ((original_time - ai_assisted_time) / original_time) * 100
        
        result = {
            "status": "success",
            "video_draft": video_structure,
            "efficiency_improvement": round(efficiency_improvement, 1),
            "materials_used": [{"id": m.id, "category": m.category} for m in matched_materials],
            "estimated_completion_time": f"{ai_assisted_time}分钟",
            "message": "视频初稿生成完成！"
        }
        
        return result
    
    def _create_video_structure(self, script: str, materials: List[VideoMaterial]) -> Dict[str, Any]:
        """创建视频结构"""
        # 将文案分成几部分（模拟剪辑结构）
        words = script.split()
        part_size = max(1, len(words) // len(materials)) if materials else 1
        
        structure = {
            "total_duration": sum(m.duration for m in materials),
            "parts": []
        }
        
        for i, material in enumerate(materials):
            start_idx = i * part_size
            end_idx = min((i + 1) * part_size, len(words))
            script_part = " ".join(words[start_idx:end_idx])
            
            structure["parts"].append({
                "part_number": i + 1,
                "material_id": material.id,
                "material_category": material.category,
                "duration": material.duration,
                "script_snippet": script_part[:50] + "..." if len(script_part) > 50 else script_part,
                "transition": "淡入淡出" if i == 0 else "交叉溶解"
            })
        
        return structure

def main():
    """主函数 - AI视频剪辑助手演示"""
    print("🎬 AI智能视频剪辑助手原型系统")
    print("模拟B端营销人员的视频制作流程\n")
    
    # 创建AI助手实例
    assistant = AIVideoAssistant()
    
    # 示例文案（模拟用户输入）
    sample_scripts = [
        "我们的新产品是一款智能手表，具有健康监测和运动追踪功能，适合追求健康生活的都市人群。",
        "春节旅游推广：展示美丽山水风景，体验传统文化，享受家庭团聚的快乐时光。",
        "公司团队建设活动，展示团队合作精神，办公室日常，商务会议场景。"
    ]
    
    # 处理每个示例文案
    for i, script in enumerate(sample_scripts, 1):
        print(f"\n处理示例 {i}:")
        print(f"文案内容: {script[:60]}...")
        
        # 生成视频初稿
        result = assistant.generate_video_draft(script)
        
        # 显示结果
        print(f"\n生成结果:")
        print(f"状态: {result['status']}")
        print(f"使用素材: {len(result['materials_used'])} 个")
        print(f"视频总时长: {result['video_draft']['total_duration']} 秒")
        print(f"效率提升: {result['efficiency_improvement']}%")
        print(f"预计完成时间: {result['estimated_completion_time']}")
        print(f"消息: {result['message']}")
        
        # 显示视频结构详情
        print("\n视频结构:")
        for part in result['video_draft']['parts']:
            print(f"  片段{part['part_number']}: {part['material_category']}素材, "
                  f"{part['duration']}秒, 文案: {part['script_snippet']}")
        
        print("=" * 50)
    
    # 模拟内测数据
    print("\n📊 内测数据模拟:")
    print("周活跃度: 85.3%")
    print("平均效率提升: 40.2%")
    print("用户满意度: 92%")
    print("\n项目原型演示完成！")

if __name__ == "__main__":
    main()