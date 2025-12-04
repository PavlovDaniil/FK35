// app/(tabs)/index.tsx
import { ThemedText } from '@/components/themed-text';
import { ThemedView } from '@/components/themed-view';
import { Link } from 'expo-router';
import { FlatList, StyleSheet } from 'react-native';

const tests = [
  { id: '1', title: 'Тест 1', href: '/tests/test1' },
  { id: '2', title: 'Тест 2', href: '/tests/test2' },
] as const;

export default function HomeScreen() {
  return (
    <ThemedView style={styles.container}>
      <ThemedText type="title">Список тестов</ThemedText>
      <FlatList
  data={tests}
  keyExtractor={(item) => item.id}
  renderItem={({ item }) => (
    <>
      <Link href={{ pathname: item.href }}>
        <ThemedText type="subtitle">{item.title}</ThemedText>
      </Link>
    </>
  )}
  ItemSeparatorComponent={() => <ThemedView style={styles.separator} />}
/>

    </ThemedView>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    padding: 16,
    gap: 16,
  },
  testItem: {
    padding: 12,
    borderRadius: 8,
    backgroundColor: '#E0E0E0', // можно заменить на динамическую тему
  },
  separator: {
    height: 12,
  },
});
